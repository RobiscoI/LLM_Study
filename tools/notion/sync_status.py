# -*- coding: utf-8 -*-
"""로드맵 Notion 페이지에 「저장소 구현 현황」 절을 쓴다.

로드맵은 '무엇을 배울지', 이 절은 '그걸 실행할 저장소가 지금 어떤 상태인지' 다.
두 가지가 한 페이지에 있어야 다음에 열었을 때 이어서 할 수 있다.

전제 (한 번만):
  1) notion.so/my-integrations -> New integration (Internal)
     - Capabilities: Read content + Insert content + Update content
  2) 로드맵 페이지 우측 상단 ... -> 연결(Connections) -> 그 인테그레이션 추가
     ★ 이걸 빼먹으면 토큰이 맞아도 404 가 난다 (Notion 은 페이지별로 권한을 준다)
  3) .env 에 NOTION_API_KEY=<Internal Integration Secret>

사용:
  python tools/notion/sync_status.py            # dry-run, 아무것도 쓰지 않는다
  python tools/notion/sync_status.py --check    # 토큰·페이지 접근만 확인
  python tools/notion/sync_status.py --apply    # 실제로 쓴다

--apply 는 같은 제목의 기존 절을 먼저 보관처리(archive)한 뒤 새로 쓴다.
Notion 의 archive 는 휴지통으로 가는 것이라 되돌릴 수 있다.
"""
import io
import json
import os
import sys
import urllib.error
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
PAGE_ID = "3e22eac0-98bd-8158-998d-e4cf925be4e6"   # LLM·Agentic AI 풀스택 24주 학습 로드맵
SECTION_TITLE = "저장소 구현 현황"

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


# ─────────────────────────────────────────────────────────────── 토큰
def load_token():
    """.env 에서만 읽는다. 값은 절대 출력하지 않는다."""
    tok = os.environ.get("NOTION_API_KEY", "").strip()
    if tok:
        return tok, "환경변수"
    path = os.path.join(REPO_ROOT, ".env")
    if not os.path.exists(path):
        return None, ".env 없음"
    for line in io.open(path, encoding="utf-8"):
        line = line.strip()
        if line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        if k.strip() == "NOTION_API_KEY":
            v = v.strip().strip('"').strip("'")
            return (v, ".env") if v else (None, ".env 에 값이 비어 있음")
    return None, ".env 에 NOTION_API_KEY 없음"


def call(token, method, path, payload=None):
    req = urllib.request.Request(
        API + path,
        method=method,
        data=json.dumps(payload).encode("utf-8") if payload is not None else None,
        headers={
            "Authorization": "Bearer " + token,
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(body)
        except ValueError:
            return e.code, {"message": body[:400]}


# ─────────────────────────────────────────────────────── 블록 만들기
def rt(text, bold=False, code=False, link=None):
    o = {"type": "text", "text": {"content": text},
         "annotations": {"bold": bold, "code": code}}
    if link:
        o["text"]["link"] = {"url": link}
    return o


def h(level, text):
    return {"object": "block", "type": "heading_%d" % level,
            "heading_%d" % level: {"rich_text": [rt(text)]}}


def para(rich):
    return {"object": "block", "type": "paragraph",
            "paragraph": {"rich_text": rich if isinstance(rich, list) else [rt(rich)]}}


def bullet(rich):
    return {"object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": rich if isinstance(rich, list) else [rt(rich)]}}


def callout(rich, emoji="⚠️"):
    return {"object": "block", "type": "callout",
            "callout": {"icon": {"type": "emoji", "emoji": emoji},
                        "rich_text": rich if isinstance(rich, list) else [rt(rich)]}}


def code(text, lang="shell"):
    return {"object": "block", "type": "code",
            "code": {"language": lang, "rich_text": [rt(text)]}}


def table(rows, header=True):
    """rows: [[cell, cell, ...], ...]  cell 은 str 또는 rich list"""
    width = len(rows[0])
    children = []
    for r in rows:
        cells = []
        for c in r:
            cells.append(c if isinstance(c, list) else [rt(c)])
        children.append({"object": "block", "type": "table_row",
                         "table_row": {"cells": cells}})
    return {"object": "block", "type": "table",
            "table": {"table_width": width, "has_column_header": header,
                      "has_row_header": False, "children": children}}


REPO_URL = "https://github.com/RobiscoI/LLM_Study"


def build_blocks():
    return [
        h(1, SECTION_TITLE),
        para([rt("이 로드맵을 실행하는 저장소: "),
              rt("RobiscoI/LLM_Study", link=REPO_URL),
              rt(" (private). 여러 PC(RJH / RMS_Digital / USER)에서 공유한다.")]),
        para([rt("로드맵이 "), rt("무엇을 배울지", bold=True),
              rt(" 라면, 이 절은 "), rt("그걸 실행할 환경이 지금 어떤 상태인지", bold=True),
              rt(" 다. 저장소 쪽 단일 진실 원천은 "), rt("CLAUDE.md", code=True), rt(" 다.")]),

        h(2, "폴더 구조"),
        para("2026-09-23 로드맵의 「저장소 구조」 절로 만들었다. 빈 폴더는 해당 주차에 도달하면 채운다 — 미리 채우지 않는 것이 요점이다."),
        table([
            ["경로", "용도", "언제"],
            ["docs/weeks/", "장별 학습 노트·세션 회고 (week-NN.md)", "매 세션"],
            ["docs/errors/", "오류 기록 (YYYY-MM-DD-제목.md)", "오류 날 때마다"],
            ["docs/PROGRESS.md", "진도표 — 이 페이지의 진도 DB 에 대응", "매주"],
            ["docs/ROADMAP.md", "이 로드맵의 Markdown 사본", "—"],
            ["docs/MCP.md", "MCP 도입 계획", "20주"],
            ["docs/architecture/", "ADR (설계 결정 기록)", "결정할 때마다"],
            ["labs/", "짧은 실습", "1–6주"],
            ["llm-from-scratch/", "tokenizer · attention · transformer", "7–9주"],
            ["apps/api/ · apps/web/", "FastAPI · Next.js", "4주 · 11주"],
            ["evals/", "golden set · 평가 스크립트", "21주"],
            ["refs/notion/", "이 로드맵 원문 (Notion 에서 내보낸 날짜별 사본)", "—"],
        ]),

        h(2, "주차 노트 템플릿"),
        para([rt("주차 노트는 "), rt("scripts/new_week.py NN", code=True), rt(" 이 "),
              rt("docs/weeks/TEMPLATE.md", code=True), rt(" 로 만든다.")]),
        para("핵심 질문 · 이론(내 말로 5문장) · 수식·손계산 · 최소 코드 · 테스트(정상·경계·실패) · 증거 · 세션 기록 · 다음 주 질문 3개"),
        callout([rt("이론·수식·코드 칸은 생성 시 비워 둔다. "),
                 rt("채워주면 노트가 아니라 교재가 되고", bold=True),
                 rt(" 로드맵의 '내 말로 바꾼다'가 무너진다.")], "📝"),

        h(2, "Claude Code 에이전트 · 스킬"),
        para("로드맵의 「GPT 프로젝트 지침」과 세 프롬프트(매일 시작 · 코드 리뷰 · 장애 분석)를 역할별로 나눈 것이다."),
        table([
            ["에이전트", "역할", "핵심 제약"],
            ["study-coach", "목적→개념→최소 코드→검증 순서로 가르침", "완성형 예제 뒤 두 번째 시도는 직접 수정. 18주차 전 프레임워크 금지"],
            ["concept-verifier", "7단계 검증 프로토콜", "손계산(3단계) 건너뛰기를 막는다"],
            ["reviewer", "위험한 문제→원인→최소 수정→테스트", "읽기 전용. 전면 재작성·스타일 지적 금지"],
            ["debugger", "사실/가설 분리 + 계층별 진단표", "이분 탐색 — 표를 다 채우지 않는다. docs/errors/ 기록"],
            ["test-writer", "정상·경계·실패 pytest 작성", "구현 코드는 수정하지 않는다"],
            ["retro-writer", "세션 회고를 docs/weeks/week-NN.md 에 기록", "하지 않은 일을 완료로 쓰지 않는다"],
        ]),
        table([
            ["스킬", "언제"],
            ["/weekly-start", "오늘 시작 — git pull 확인 → 수준 확인 질문 3개 → 계획"],
            ["/explain-concept", "개념 하나를 8단계로 설명"],
            ["/verify", "개념·수식이 막힐 때 (7단계)"],
            ["/debug-trace", "동작이 안 될 때 (사실/가설 분리)"],
            ["/code-review", "코드 제출"],
            ["/weekly-retro", "오늘 마무리 — 회고 기록 + 커밋 안내"],
            ["/weekly-close", "장 마감 — 체크리스트 7항목 + 회고"],
            ["/assess", "이해도 5수준 판정"],
        ]),

        h(2, "환경 준비 현황"),
        para("학습과 별개로 미리 깔아둬야 해당 주차에 막히지 않는 것들."),
        table([
            ["항목", "필요 시점", "RMS_Digital", "RJH", "USER"],
            ["Python 3.12", "1주", "✅ 3.12.10", "☐", "✅ 3.14.4"],
            ["git · VS Code", "1주", "✅", "✅", "✅"],
            ["Node.js LTS", "11주 (+ MCP 전제)", "❌", "❌", "✅ 24.15.0"],
            ["Docker Desktop", "14주 선택", "❌", "❌", "✅ 29.8.2"],
            ["PostgreSQL (Docker)", "14주 선택", "❌", "❌", "❌"],
            ["gh CLI", "23주", "❌", "❌", "✅ 2.102.0"],
        ]),
        callout([rt("Node.js 가 11주차(Next.js)뿐 아니라 "),
                 rt("대부분의 MCP 서버(npx 기반)의 전제", bold=True),
                 rt(" 다. RMS_Digital·RJH 에는 아직 없어 그 PC 에서는 MCP 를 붙일 수 없다 (USER 는 설치됨).")]),

        h(2, "MCP — 20주차까지 비워 둔다"),
        para([rt(".mcp.json", code=True),
              rt(" 은 커밋되는 프로젝트 스코프 설정이라 git pull 만으로 모든 PC 가 같은 구성을 쓴다. 지금은 "),
              rt("의도적으로 비어 있다", bold=True), rt(".")]),
        bullet([rt("MCP 는 20주차 학습 내용 그 자체다 — 남의 서버를 미리 붙이면 직접 만드는 경험이 희석된다")]),
        bullet([rt("로드맵 원칙과 같은 맥락: "),
                rt("에이전트 프레임워크를 쓰기 전에 작은 agent loop 를 직접 구현한다", bold=True)]),
        bullet([rt("MCP 서버는 켜두는 것만으로 도구 정의가 매 요청에 실려 컨텍스트를 먹는다")]),
        para("도입 예정: 11주~ Context7(라이브러리 문서) · 14주~ PostgreSQL(선택 경로) · 20주 직접 만든 서버 · 21주~ Playwright."),

        h(2, "여러 PC 공유 방식"),
        para([rt("절대경로를 코드·문서에 박지 않는다. PC 의존 값은 "),
              rt("tools/study-config/study-config.json", code=True),
              rt(" 의 hosts 블록 한 곳에만 둔다. "),
              rt("resolve.ps1", code=True),
              rt(" 이 USERNAME 으로 현재 PC 를 판정해 Python·venv·.env·데이터 경로를 해석하고, git pull/checkout 직후 훅이 자동 실행한다.")]),
        code("git clone https://github.com/RobiscoI/LLM_Study.git\n"
             "cd LLM_Study\n"
             "git config core.hooksPath .githooks\n"
             "cp .env.example .env          # API 키는 PC 마다 따로\n"
             "python -m venv .venv\n"
             ".venv/Scripts/pip install -r requirements.txt", "shell"),
        callout([rt(".env", code=True), rt(" 와 "), rt(".venv", code=True),
                 rt(" 는 git 으로 오가지 않는다. API 키는 절대 커밋하지 않는다.")], "🔑"),

        h(2, "이 절은 스크립트로 갱신한다"),
        para([rt("손으로 고치지 말 것 — "), rt("tools/notion/sync_status.py", code=True),
              rt(" 가 같은 제목의 절을 보관처리한 뒤 다시 쓴다. 저장소가 바뀌면 스크립트를 고치고 다시 돌린다.")]),
        code("python tools/notion/sync_status.py --check\n"
             "python tools/notion/sync_status.py --apply", "shell"),
    ]


# ─────────────────────────────────────────────────────────────── 실행
def find_section(token, page_id):
    """같은 제목의 heading_1 과 그 뒤 블록들(다음 heading_1 전까지)의 id 목록."""
    ids, cursor, found = [], None, False
    while True:
        q = "?page_size=100" + (("&start_cursor=" + cursor) if cursor else "")
        st, d = call(token, "GET", "/blocks/%s/children%s" % (page_id, q))
        if st != 200:
            return None, d
        for b in d.get("results", []):
            t = b.get("type")
            if t == "heading_1":
                txt = "".join(x.get("plain_text", "")
                              for x in b["heading_1"].get("rich_text", []))
                if txt.strip() == SECTION_TITLE:
                    found = True
                    ids.append(b["id"])
                    continue
                if found:
                    return ids, None          # 다음 heading_1 에서 끝
            if found:
                ids.append(b["id"])
        if not d.get("has_more"):
            return ids, None
        cursor = d.get("next_cursor")


def main():
    apply_ = "--apply" in sys.argv
    check_ = "--check" in sys.argv

    token, src = load_token()
    print("토큰 출처 : %s" % src)
    if not token:
        print("\n토큰이 없다. 아래를 먼저 하고 다시 실행할 것:")
        print("  1) notion.so/my-integrations -> New integration (Internal)")
        print("     Capabilities: Read + Insert + Update content")
        print("  2) 로드맵 페이지 ... -> 연결(Connections) -> 그 인테그레이션 추가")
        print("  3) .env 에 NOTION_API_KEY=<secret>")
        return 3
    print("토큰 길이 : %d" % len(token))

    st, me = call(token, "GET", "/users/me")
    if st != 200:
        print("인증 실패 HTTP %s : %s" % (st, me.get("message")))
        return 4
    bot = me.get("bot") or {}
    print("인테그레이션: %s" % me.get("name"))
    print("워크스페이스: %s" % (bot.get("workspace_name") or "(미상)"))

    st, pg = call(token, "GET", "/pages/" + PAGE_ID)
    if st != 200:
        print("\n페이지 접근 실패 HTTP %s : %s" % (st, pg.get("message")))
        if st == 404:
            print("→ 토큰은 유효하지만 이 페이지에 '연결'이 안 돼 있다.")
            print("  로드맵 페이지 우측 상단 ... -> 연결(Connections) -> 인테그레이션 추가")
        return 5
    title = ""
    for v in (pg.get("properties") or {}).values():
        if v.get("type") == "title":
            title = "".join(x.get("plain_text", "") for x in v["title"])
    print("페이지     : %s" % title)

    blocks = build_blocks()
    print("쓸 블록    : %d 개" % len(blocks))

    old, err = find_section(token, PAGE_ID)
    if err:
        print("기존 절 조회 실패: %s" % err.get("message"))
        return 6
    print("기존 절    : %s" % ("없음" if not old else "%d 블록 (보관처리 대상)" % len(old)))

    if check_ or not apply_:
        print("\n[dry-run] 아무것도 쓰지 않았다. 실제 반영은 --apply")
        return 0

    for bid in old:
        call(token, "PATCH", "/blocks/" + bid, {"archived": True})
    if old:
        print("보관처리   : %d 블록 (Notion 휴지통에서 복구 가능)" % len(old))

    # 한 번에 100개까지
    for i in range(0, len(blocks), 90):
        st, d = call(token, "PATCH", "/blocks/%s/children" % PAGE_ID,
                     {"children": blocks[i:i + 90]})
        if st != 200:
            print("쓰기 실패 HTTP %s : %s" % (st, d.get("message")))
            return 7
    print("완료       : https://www.notion.so/%s" % PAGE_ID.replace("-", ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
