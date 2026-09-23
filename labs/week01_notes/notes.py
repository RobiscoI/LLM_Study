"""Core logic for a small file-backed notes application.

The module deliberately keeps storage and command-line concerns separate so the
data rules can be tested without starting a subprocess.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import TypedDict


class Note(TypedDict):
    """A single persisted note."""

    id: int
    content: str


class NotesError(Exception):
    """Base exception for expected notes application failures."""


class EmptyNoteError(NotesError):
    """Raised when a user tries to save an empty note."""


class InvalidNotesFileError(NotesError):
    """Raised when the notes file is not valid JSON or has an invalid schema."""


def _validate_notes(value: object) -> list[Note]:
    if not isinstance(value, list):
        raise InvalidNotesFileError("메모 파일의 최상위 값은 JSON 배열이어야 합니다.")

    notes: list[Note] = []
    seen_ids: set[int] = set()
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise InvalidNotesFileError(f"{index}번 메모는 JSON 객체여야 합니다.")

        note_id = item.get("id")
        content = item.get("content")
        if isinstance(note_id, bool) or not isinstance(note_id, int) or note_id < 1:
            raise InvalidNotesFileError(f"{index}번 메모의 id는 1 이상의 정수여야 합니다.")
        if note_id in seen_ids:
            raise InvalidNotesFileError(f"중복된 메모 id가 있습니다: {note_id}")
        if not isinstance(content, str) or not content.strip():
            raise InvalidNotesFileError(f"{index}번 메모의 content는 비어 있지 않은 문자열이어야 합니다.")

        seen_ids.add(note_id)
        notes.append({"id": note_id, "content": content})

    return notes


def load_notes(path: Path) -> list[Note]:
    """Load and validate notes, returning an empty list when the file is absent."""

    if not path.exists():
        return []

    try:
        raw_value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise InvalidNotesFileError(
            f"메모 파일이 올바른 JSON이 아닙니다: {error.msg} (line {error.lineno})"
        ) from error
    except OSError as error:
        raise NotesError(f"메모 파일을 읽을 수 없습니다: {error}") from error

    return _validate_notes(raw_value)


def save_notes(path: Path, notes: list[Note]) -> None:
    """Validate and atomically save notes as UTF-8 JSON."""

    validated = _validate_notes(notes)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(f"{path.suffix}.tmp")

    try:
        temporary_path.write_text(
            json.dumps(validated, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        temporary_path.replace(path)
    except OSError as error:
        raise NotesError(f"메모 파일을 저장할 수 없습니다: {error}") from error


def add_note(notes: list[Note], content: str) -> Note:
    """Append a non-empty note and return the new record."""

    normalized_content = content.strip()
    if not normalized_content:
        raise EmptyNoteError("메모 내용은 비어 있을 수 없습니다.")

    next_id = max((note["id"] for note in notes), default=0) + 1
    note: Note = {"id": next_id, "content": normalized_content}
    notes.append(note)
    return note


def delete_note(notes: list[Note], note_id: int) -> bool:
    """Delete a note by id and report whether it existed."""

    for index, note in enumerate(notes):
        if note["id"] == note_id:
            del notes[index]
            return True
    return False


def search_notes(notes: list[Note], query: str) -> list[Note]:
    """Return notes containing the query using case-insensitive matching."""

    normalized_query = query.strip().casefold()
    if not normalized_query:
        return []
    return [note for note in notes if normalized_query in note["content"].casefold()]
