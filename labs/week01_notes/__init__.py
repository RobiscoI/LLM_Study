"""Week 1 file-backed notes application."""

from .notes import (
    EmptyNoteError,
    InvalidNotesFileError,
    add_note,
    delete_note,
    load_notes,
    save_notes,
    search_notes,
)

__all__ = [
    "EmptyNoteError",
    "InvalidNotesFileError",
    "add_note",
    "delete_note",
    "load_notes",
    "save_notes",
    "search_notes",
]
