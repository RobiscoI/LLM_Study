"""새 주차 폴더와 노트를 템플릿에서 만든다.

사용법 (저장소 루트에서):
    python scripts/new_week.py 02
    python scripts/new_week.py 12 "React·Next.js"

만드는 것:
    lessons/week02/README.md   본문 독립 예제 폴더 + 설명
    lessons/week02/tests/      테스트 폴더
    docs/weeks/week-02.md       학습 노트 (docs/weeks/TEMPLATE.md 복사)
이미 있으면 덮어쓰지 않는다.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    week = sys.argv[1].lower().lstrip("week-").zfill(2)  # "2" -> "02", "12a" -> "12a"
    title = sys.argv[2] if len(sys.argv) > 2 else f"Week {week}"

    code_dir = ROOT / "lessons" / f"week{week}"
    tests_dir = code_dir / "tests"
    note = ROOT / "docs" / "weeks" / f"week-{week}.md"
    template = ROOT / "docs" / "weeks" / "TEMPLATE.md"

    tests_dir.mkdir(parents=True, exist_ok=True)
    (tests_dir / "__init__.py").touch(exist_ok=True)

    readme = code_dir / "README.md"
    if not readme.exists():
        readme.write_text(
            f"# lessons/week{week}: {title}\n\n"
            f"## 실행\n```powershell\n# 프로젝트 루트에서\npython lessons/week{week}/main.py\npython -m pytest -q lessons/week{week}\n```\n\n"
            "## 파일\n- `main.py` — \n- `tests/` — 정상·경계·실패 테스트\n",
            encoding="utf-8",
        )
        print(f"만듦: {readme.relative_to(ROOT)}")
    else:
        print(f"이미 있음: {readme.relative_to(ROOT)}")

    if not note.exists():
        text = template.read_text(encoding="utf-8").replace("Week NN", f"Week {week}", 1)
        text = text.replace("<주제>", title, 1).replace("week-NN", f"week-{week}")
        note.write_text(text, encoding="utf-8")
        print(f"만듦: {note.relative_to(ROOT)}")
    else:
        print(f"이미 있음: {note.relative_to(ROOT)}")

    print("\n다음: docs/progress.md 에서 상태를 '진행'으로 바꾸고 시작일을 적는다.")


if __name__ == "__main__":
    main()
