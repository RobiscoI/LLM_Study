# Week 01 — 개발 환경과 Python: CLI 메모 앱

로드맵 행: 개발 환경과 Python / CLI 메모 앱 (기존 실습: `labs/week01_notes`) / 완료 기준은 Notion 1장 본문 확인 필요 (이번 세션에서 읽지 않음)

## 핵심 질문 (이 주가 끝나면 답할 수 있어야 하는 것)
1. `python`과 `.venv\Scripts\python.exe`는 어떻게 다르고, 어떤 명령으로 확인하는가?
2. `load_notes`는 파일이 없으면 `[]`, 스키마가 잘못되면 예외로 처리한다. 왜 다르게 다루는가? 실행 중과 종료 후 데이터는 각각 어떤 형태이고 어디에 있는가?
3. `_validate_notes`는 왜 bool을 따로 검사하는가? (`isinstance(True, int)`)

## 이론 — 내 말로 5문장
- 아직 작성 전. 이번 세션(2026-10-23)에는 1장 개념 정리를 하지 않았다.

## 수식·손계산 (해당 시)
해당 없음.

## 최소 코드
- 위치: `lessons/week01/` (아직 없음. `scripts/new_week.py 01` 미실행). 기존 실습은 `labs/week01_notes/` (`notes.py`, `cli.py`, `test_notes.py`)
- 실행: 다음 세션 첫 단계로 `python -m pytest -q labs/week01_notes`
- 예상 결과: 7개 통과 (`docs/progress.md` 기록 기준. 이번 세션에서 재실행하지 않았음)

## 테스트 (정상·경계·실패)
| 종류 | 입력 | 기대 | 결과 |
|---|---|---|---|
| 정상 | | | 이번 세션 미실행 |
| 경계 | | | 이번 세션 미실행 |
| 실패 | | | 이번 세션 미실행 |

## 증거 (docs/evidence/ 링크)
- 없음

## 세션 기록

### 2026-10-23 (약 10분)
**한 일**
- `/weekly-start`: `docs/progress.md` 확인, 현재 1장(학습 중). `docs/weeks/week-01.md`, `lessons/week01/`은 아직 없었음. `scripts/new_week.py 01`은 실행하지 않음.
- `git status`와 `git fetch`로 origin/main과 차이 없음을 확인 (pull 불필요). 커밋 안 된 변경이 다수 있음 (`.claude/` agents·skills·hooks, `docs/` 신규 문서, `scripts/` 등).
- LF→CRLF 경고는 `.gitattributes`에 따른 줄바꿈 변환 안내이며 오류가 아님을 설명받음.
- 채팅에 `git add lessons/week00`을 텍스트로만 적으면 실행되지 않음을 확인. `!` 접두사로 실행하는 방법을 배움.
- `! git add lessons/week00`으로 스테이징 후 `M inspect_runtime.py`, `A observe_process.py` 확인.
- `git commit` 성공: `6345b1b` "week-00: observe_process.py 추가, inspect_runtime.py 수정" (2 files, 16 insertions). 아직 push 안 함.
- 1장 개념·코드 실습은 하지 않음. 이번 세션은 환경·Git 정리만 진행.

**배운 것 (내 말로 5문장 이내)**
- `git add`는 커밋할 파일을 고르는 스테이징(staging)이다.
- `git commit`은 스테이징된 내용을 이력으로 기록한다. `git push` 전까지는 로컬 PC에만 존재한다.
- `git fetch` 후 `git status`로 원격보다 뒤처졌는지(behind) 확인한다.
- `git diff --name-status`의 `M`은 수정, `A`는 추가를 뜻한다.
- 채팅 입력은 셸 명령이 아니므로, 직접 실행하려면 `!`를 앞에 붙인다.

**막힌 점·미해결**
- 수준 확인 질문 3개 미응답 (다음 세션에 다시 묻는다). 위 "핵심 질문" 1~3번과 같다.
- 나머지 변경(코치 구조·문서)은 아직 커밋하지 않았고 `git push`도 하지 않음.
- `labs/week01_notes` 테스트 7개는 progress.md 기록만 있고 이번 세션에서 재현하지 못함.

**완료 체크리스트** (로드맵 기준)
- [ ] 핵심 개념을 내 말로 정리 (미실시)
- [ ] 예제를 직접 입력하고 실행 (미실시)
- [ ] 미니 프로젝트/기능 완료 (확인 필요: 기존 `labs/week01_notes`가 있으나 이번 세션 증거 없음)
- [ ] 테스트와 예상 결과 기록 (미실시)
- [ ] 오류 원인과 해결 과정 기록 (docs/errors/) (해당 오류 없음, 미실시)
- [ ] Git 커밋·README 갱신 (확인 필요: 이번 커밋은 week-00 대상이며 1장 기준 아님)
- [ ] 다음 주 질문 3개 (미실시)

**다음 행동 3개**
1. [다음 세션 첫 10분] `git status` / `git fetch`로 상태를 확인한 뒤, `python -m pytest -q labs/week01_notes`를 실행해 7개 통과를 재현한다. (`python labs/week01_notes/test_notes.py`가 아님)
2. 수준 확인 질문 3개에 답한다.
3. `python scripts/new_week.py 01`을 직접 실행해 `lessons/week01`을 만들고, 1장 본문 1절(목적과 상황)부터 시작한다.

다음 세션: 2026-10-28(수)부터 재개.

## 다음 주 질문 3개
1. (1장 완료 후 작성)
2. 
3. 
