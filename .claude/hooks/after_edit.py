"""Claude 가 .py 파일을 수정하면 자동으로 문법 검사를 한다 (Windows·macOS·Linux 공통).

실패하면 종료 코드 2로 끝나 Claude 에게 오류가 전달되고, 바로 고치게 된다.
입력(JSON)은 stdin 으로 들어온다. 파싱이 안 되면 조용히 통과한다.
"""

import json
import py_compile
import sys


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    path = (payload.get("tool_input") or {}).get("file_path", "")
    if not path.endswith(".py"):
        return 0
    try:
        py_compile.compile(path, doraise=True)
    except py_compile.PyCompileError as exc:
        print(f"py_compile 실패: {path}\n{exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
