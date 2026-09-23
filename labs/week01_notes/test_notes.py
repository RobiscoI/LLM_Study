"""Tests for the week 1 notes application.

These tests run with both the standard library's unittest runner and pytest.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from labs.week01_notes.notes import (
    EmptyNoteError,
    InvalidNotesFileError,
    add_note,
    delete_note,
    load_notes,
    save_notes,
    search_notes,
)


class NotesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.database_path = Path(self.temporary_directory.name) / "notes.json"

    def test_missing_file_returns_empty_list(self) -> None:
        self.assertEqual(load_notes(self.database_path), [])

    def test_korean_note_round_trip(self) -> None:
        notes = []
        created = add_note(notes, "  첫 번째 한글 메모  ")
        save_notes(self.database_path, notes)

        self.assertEqual(created, {"id": 1, "content": "첫 번째 한글 메모"})
        self.assertEqual(load_notes(self.database_path), [created])

    def test_empty_note_is_rejected(self) -> None:
        with self.assertRaisesRegex(EmptyNoteError, "비어 있을 수 없습니다"):
            add_note([], "   ")

    def test_delete_reports_found_and_missing_ids(self) -> None:
        notes = [{"id": 1, "content": "keep"}, {"id": 2, "content": "delete"}]

        self.assertTrue(delete_note(notes, 2))
        self.assertFalse(delete_note(notes, 99))
        self.assertEqual(notes, [{"id": 1, "content": "keep"}])

    def test_search_is_case_insensitive(self) -> None:
        notes = [
            {"id": 1, "content": "Learn FastAPI"},
            {"id": 2, "content": "learn Python"},
            {"id": 3, "content": "Read a paper"},
        ]

        self.assertEqual(search_notes(notes, "LEARN"), notes[:2])
        self.assertEqual(search_notes(notes, "   "), [])

    def test_corrupted_json_has_a_clear_error(self) -> None:
        self.database_path.write_text("[{broken", encoding="utf-8")

        with self.assertRaisesRegex(InvalidNotesFileError, "올바른 JSON"):
            load_notes(self.database_path)

    def test_invalid_schema_is_rejected(self) -> None:
        self.database_path.write_text(
            '[{"id": 1, "content": "ok"}, {"id": 1, "content": "duplicate"}]',
            encoding="utf-8",
        )

        with self.assertRaisesRegex(InvalidNotesFileError, "중복된 메모 id"):
            load_notes(self.database_path)


if __name__ == "__main__":
    unittest.main()
