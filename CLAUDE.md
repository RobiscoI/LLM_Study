# LLM·Agentic AI 풀스택 24주 학습 — 프로젝트 메모리

## 이 저장소는 무엇인가

Notion 로드맵 「LLM·Agentic AI 풀스택 24주 학습 로드맵」을 실행하는 저장소다.
원문은 `refs/notion/로드맵_전문_20260923.md` 에 그대로 보관한다 — **로드맵이 단일 진실
원천이고, 이 파일은 그것을 저장소 규약으로 옮긴 것이다.**

- **목표**: LLM 의 원리와 코드를 이해하고, 프론트엔드·백엔드·DB·네트워크·배포·Agentic AI 를
  직접 연결하여 실제 앱을 만든다.
- **24주 후 결과물**: Python 으로 토큰화·어텐션을 구현하고, Next.js + FastAPI + PostgreSQL
  기반의 스트리밍 RAG/Agent 앱을 안전하게 배포한다.
- **최종 프로젝트**: 개인 지식 기반 AI 업무 도우미.

## 학습 원칙 (에이전트가 반드시 지킬 것)

로드맵이 정한 교습 방식이다. 이것을 어기면 학습이 아니라 대필이 된다.

1. **완성 코드를 즉시 전부 주지 않는다.** 생각할 작은 단계와 힌트를 먼저 준다.
2. **설명 순서 고정**: 개념 → 왜 필요한가 → 요청/데이터 흐름 → 최소 코드 → 실행 방법 →
   예상 결과 → 흔한 오류 → 확인 문제.
3. **모르는 것은 추측하지 않는다.** 확인 방법을 알려준다.
4. **세션 끝에는** 학습 요약 · 완료 체크리스트 · 막힌 점 · 다음 행동 3개를 남긴다.
5. **예제를 복사했으면 반드시 기능 하나를 바꾼다.** 오류 원인과 해결 과정을 기록한다.
6. **코드 결과를 증명으로 착각하지 않는다.** 반례 가능성을 따로 기록한다.

> 시간 배분은 **개념 20% · 코딩 60% · 검증/회고 20%**.
> 주당 7~10시간 (개념 2h → 따라 치기 2h → 직접 구현 3~5h → 회고 1h).

## 24주 단계

| 단계 | 주차 | 핵심 결과물 |
|---|---|---|
| 컴퓨팅·웹 기초 | 0–4 | 터미널·Python·자료구조·네트워크·CRUD API |
| ML·LLM 원리 | 5–10 | 경사하강·역전파·tokenizer·attention·LLM API |
| 풀스택 LLM 앱 | 11–14 | Next.js UI·streaming·PostgreSQL·인증 |
| RAG·Agent | 15–20 | 검색·RAG·도구·agent loop·MCP |
| 품질·보안·배포 | 21–24 | 평가·위협 모델·CI/CD·최종 프로젝트 |

주차별 개념·실습·완료 기준은 `docs/ROADMAP.md` 의 표를 본다.

### 포트폴리오 관문 (여기서 막히면 다음 단계로 가지 않는다)

| 주차 | 산출물 |
|---|---|
| 4 | FastAPI 메모 CRUD — HTTP, REST, pytest |
| 10 | CLI LLM 챗봇 — 프롬프트, 구조화 출력, 비용·오류 처리 |
| 14 | 로그인 가능한 풀스택 채팅 — Next.js, SSE, PostgreSQL, Auth |
| 16 | 출처 기반 문서 Q&A — embedding, vector search, RAG |
| 20 | 승인 가능한 업무 에이전트 — tools, workflow, MCP, trace |
| 24 | 운영형 AI 앱 — 보안, 평가, Docker, CI/CD, 배포 |

## 폴더 구조

로드맵의 「저장소 구조」를 그대로 따른다 (`ai-learning/` → 이 저장소).

```
LLM_Study/
├─ CLAUDE.md                  이 파일
├─ docs/
│  ├─ ROADMAP.md              24주 표 + 운영 방식
│  ├─ weekly/                 ★ 주차 노트 — 9절 템플릿 (_TEMPLATE.md)
│  └─ architecture/           아키텍처·설계 결정
├─ labs/                      주차별 짧은 실습 (앱에 안 들어가는 것)
├─ llm-from-scratch/          tokenizer·attention·transformer (7–9주)
├─ apps/
│  ├─ api/                    FastAPI (4주~)
│  └─ web/                    Next.js (11주~)
├─ packages/shared/           공통 타입·스키마
├─ evals/                     평가 데이터·스크립트 (21주~)
├─ refs/
│  ├─ notion/                 ★ 로드맵 원문 (수정 금지)
│  └─ papers/                 논문·자료
├─ tools/study-config/        PC 별 경로 해석
└─ .claude/{agents,skills}/
```

> `apps/`·`packages/`·`evals/` 는 해당 주차에 도달하면 채운다. 지금은 `.gitkeep` 만 있다.
> **미리 채우지 않는다** — 로드맵이 각 주차에 그것을 직접 만들라고 시키는 것이 학습이다.

## 주차 노트 — 9절 구조 (로드맵이 정한 형식)

`docs/weekly/W<NN>_<주제>.md`. 선수 주차 페이지가 이 형식의 기준이다
(`refs/notion/선수주차_원문_20260923.md`).

| 절 | 내용 |
|---|---|
| 1 | 선수지식과 핵심 질문 |
| 2 | 이론을 쉽게 잡기 |
| 3 | 수식·유도·증명 |
| 4 | 눈으로 이해하기 (mermaid) |
| 5 | 직접 구현 |
| 6 | 검증 계획 (표: 방법 / 검증 / 통과 기준) |
| 7 | 미니 프로젝트 |
| 8 | 완료 체크리스트 |
| 9 | 이해 확인 (질문 3개) |

`/weekly-note` 스킬이 이 뼈대를 만든다.

## 수식·증명·코드 검증 프로토콜 (7단계, 건너뛰지 말 것)

```
정의·가정 → shape·단위 확인 → 작은 수 손계산 → 코드 구현
          → 수치/자동 테스트 → 경계·반례 → 결론·한계
```

1. **정의**: 기호가 무엇을 뜻하는지와 가정을 먼저 적는다.
2. **유도**: 등호 한 줄마다 사용한 법칙을 적는다.
3. **손계산**: 2×2 행렬이나 3개 토큰처럼 작은 입력으로 계산한다.
4. **수치 검증**: analytic 결과와 finite difference·brute force·기준 구현을 비교한다.
5. **반례**: 빈 입력, 0, 매우 큰 값, 잘못된 타입, 연결 끊김을 넣는다.
6. **설명**: 결과가 맞다는 사실과 왜 맞는지, 적용 한계를 분리한다.

> 수학이 막히면 작은 tensor shape 와 숫자로 현상을 먼저 확인한 뒤 일반식으로 돌아온다.

## 이해도 5수준 (완료 판정 척도)

| 수준 | 판정 |
|---|---|
| 1 기억 | 용어를 정의한다 |
| 2 이해 | 왜 필요한지 자신의 말로 설명한다 |
| 3 적용 | 예제 없이 작은 기능을 구현한다 |
| 4 분석 | 로그와 통신 흐름으로 오류를 찾는다 |
| 5 설계 | 보안·비용·성능 trade-off 를 근거로 선택한다 |

**주차 완료 = 최소 3수준.** 포트폴리오 관문 주차(4·10·14·16·20·24)는 **4수준 이상**.

## 권장 기술 스택

| 영역 | 스택 |
|---|---|
| 언어 | Python, TypeScript |
| 프론트 | React, Next.js, Tailwind CSS |
| 백엔드 | FastAPI, Pydantic, SQLAlchemy |
| 데이터 | PostgreSQL, pgvector, Redis |
| 통신 | REST, SSE, WebSocket |
| 테스트 | pytest, Playwright |
| 운영 | Docker, GitHub Actions, HTTPS, observability |

> **중요 원칙: 에이전트 프레임워크를 쓰기 전에 작은 agent loop 를 직접 구현한다.**
> LangChain·LlamaIndex 등을 18주차 전에 끌어오지 않는다.

## 에이전트 · 스킬

| 에이전트 | 역할 |
|---|---|
| `study-coach` | 로드맵 기준 학습 코치. 8단계 설명 순서, 힌트 우선 |
| `code-reviewer` | 정확성·보안·가독성·테스트·네트워크 관점 리뷰 |
| `incident-analyst` | 사실/가설 분리, 브라우저→네트워크→백엔드→DB/LLM 순 진단 |
| `concept-verifier` | 7단계 검증 프로토콜 실행. 손계산·반례 담당 |

| 스킬 | 역할 |
|---|---|
| `/daily` | 오늘 학습 시작 — 수준 확인 질문 3개 → 20/60/20 진행 |
| `/weekly-note` | 주차 노트 9절 뼈대 생성 |
| `/weekly-close` | 주차 마감 — 체크리스트·회고·다음 주 질문 3개 |
| `/verify` | 수식·코드 7단계 검증 |
| `/review` | 코드 리뷰 |
| `/debug` | 장애 분석 (사실/가설 분리 + 진단표) |
| `/assess` | 이해도 5수준 판정 + 확인 문제 |

## 두 PC 공유 (RJH / RMS_Digital)

DF 저장소와 같은 규약이다. **절대경로를 코드·문서에 직접 박지 않는다.**
PC 의존 값은 `tools/study-config/study-config.json` 의 `hosts` 블록 한 곳에만 둔다.

```powershell
powershell -ExecutionPolicy Bypass -File tools/study-config/resolve.ps1
powershell -ExecutionPolicy Bypass -File tools/study-config/resolve.ps1 -Json
```

현재 PC 는 `USERNAME` 으로 판정한다. `git pull` / `git checkout` 직후에는
`.githooks/post-merge`·`post-checkout` 이 자동 실행한다
(새 클론에서 한 번만 `git config core.hooksPath .githooks`).

| | `RJH` | `RMS_Digital` |
|---|---|---|
| repo | `C:/Users/RJH/Desktop/LLM_Study` | `C:/Users/RMS_Digital/Desktop/LLM_Study` |
| Python | PATH 의 python | 3.12.10 |
| 대용량 | (미설정) | `D:/LLM_Data` |

**`.env` 와 `.venv` 는 git 으로 오가지 않는다.** 각 PC 에서 따로 만든다
(`.env.example` 복사). API 키는 절대 커밋하지 않는다.

## 인코딩 규약 (두 PC 다 Windows — 어기면 조용히 깨진다)

| 확장자 | 인코딩 | 줄바꿈 |
|---|---|---|
| `.ps1` | UTF-8 **BOM 필수** | CRLF |
| `.sh` · `.githooks/*` | UTF-8 (BOM 금지) | LF |
| `.py` · `.md` · `.json` · `.ts` | UTF-8 (BOM 없음) | LF |

- `.ps1` 에 BOM 이 없으면 Windows PowerShell 5.1 이 CP949 로 오해석해 **한글이 든 줄이
  통째로 사라진다.**
- `.sh` 에 BOM 이 붙으면 Git Bash 가 셔뱅을 못 읽는다.
- `.gitattributes` 가 줄바꿈은 강제하지만 **BOM 은 강제하지 못한다** — 직접 챙길 것.
- 훅 파일은 확장자가 없어 `*.sh` 규칙에 안 걸린다. `.githooks/*` 규칙이 따로 있다.

## 진도 조정 (로드맵 규정)

- Python 이 처음이면 1~4주를 각각 2주로 확장한다.
- 웹 경험이 있으면 11~12주를 합치고 테스트·보안 시간을 늘린다.
- 수학에서 막히면 증명보다 작은 수와 tensor shape 로 먼저 검증한다.
- 주당 5시간 미만이면 36주로 늘리되 **프로젝트 범위는 유지한다.**
- 라이브러리 암기보다 HTTP·상태·데이터 흐름·평가 원리를 우선한다.

## 표준 작업 절차

1. 오늘 시작: `/daily`
2. 새 주차 시작: `/weekly-note` → `docs/weekly/W<NN>_<주제>.md` 생성
3. 막히면: `/verify` (개념·수식) 또는 `/debug` (동작 오류)
4. 코드 제출: `/review`
5. 주차 마감: `/weekly-close` → `/assess`
6. 커밋. 로드맵 체크리스트에 **Git 커밋·README 업데이트**가 매주 들어 있다.
