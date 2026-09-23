"""Command-line interface for the week 1 notes application."""

from __future__ import annotations

import argparse
from pathlib import Path

from .notes import NotesError, add_note, delete_note, load_notes, save_notes, search_notes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="파일 기반 CLI 메모 앱")
    parser.add_argument(
        "--db",
        type=Path,
        default=Path("notes.json"),
        help="메모 JSON 경로 (기본값: notes.json)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="메모 추가")
    add_parser.add_argument("content", help="저장할 메모 내용")

    subparsers.add_parser("list", help="전체 메모 조회")

    delete_parser = subparsers.add_parser("delete", help="메모 삭제")
    delete_parser.add_argument("id", type=int, help="삭제할 메모 id")

    search_parser = subparsers.add_parser("search", help="메모 검색")
    search_parser.add_argument("query", help="검색할 문자열")
    return parser


def _print_notes(notes: list[dict[str, object]]) -> None:
    if not notes:
        print("메모가 없습니다.")
        return
    for note in notes:
        print(f"{note['id']}: {note['content']}")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        notes = load_notes(args.db)
        if args.command == "add":
            note = add_note(notes, args.content)
            save_notes(args.db, notes)
            print(f"추가됨: {note['id']}")
        elif args.command == "list":
            _print_notes(notes)
        elif args.command == "delete":
            if not delete_note(notes, args.id):
                print(f"메모를 찾을 수 없습니다: {args.id}")
                return 1
            save_notes(args.db, notes)
            print(f"삭제됨: {args.id}")
        elif args.command == "search":
            _print_notes(search_notes(notes, args.query))
    except NotesError as error:
        print(f"오류: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
