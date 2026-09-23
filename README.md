# LLM_Study

**LLM·Agentic AI 풀스택 24주 학습 로드맵**을 실행하는 저장소.
두 대의 PC(`RJH` / `RMS_Digital`)에서 공유한다.

> **목표** — LLM 의 원리와 코드를 이해하고, 프론트엔드·백엔드·DB·네트워크·배포·
> Agentic AI 를 직접 연결하여 실제 앱을 만든다.
> **24주 후** — Python 으로 토큰화·어텐션을 구현하고, Next.js + FastAPI + PostgreSQL
> 기반의 스트리밍 RAG/Agent 앱을 안전하게 배포한다.

로드맵 전문은 [`docs/ROADMAP.md`](docs/ROADMAP.md), 원문은 `refs/notion/`.
작업 규약은 [`CLAUDE.md`](CLAUDE.md).

## 새 PC 에서 처음 한 번

```bash
git clone https://github.com/RobiscoI/LLM_Study.git
cd LLM_Study
git config core.hooksPath .githooks     # pull/checkout 후 경로 자동 점검
cp .env.example .env                    # 그리고 API 키를 채운다
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt
```

`.env` 와 `.venv` 는 **git 으로 오가지 않는다.** 각 PC 에서 따로 만든다.

## 매번

```powershell
powershell -ExecutionPolicy Bypass -File tools/study-config/resolve.ps1
```

현재 PC 를 판정해서 Python·venv·`.env`·데이터 경로를 해석해 보여준다.
`git pull` / `git checkout` 직후에는 훅이 자동 실행한다.

**절대경로를 코드나 문서에 직접 박지 않는다.** PC 의존 값은
`tools/study-config/study-config.json` 의 `hosts` 블록 한 곳에만 둔다.

## 학습 흐름

| 단계 | 명령 |
|---|---|
| 새 주차 시작 | `/weekly-note` → `docs/weekly/W<NN>_<주제>.md` 생성 |
| 오늘 시작 | `/daily` — 수준 확인 질문 3개 → 개념 20% / 코딩 60% / 검증·회고 20% |
| 개념이 막힘 | `/verify` — 7단계 검증 (손계산·반례) |
| 동작이 안 됨 | `/debug` — 사실/가설 분리 + 계층별 진단표 |
| 코드 제출 | `/review` — 위험한 문제 → 원인 → 최소 수정 → 테스트 |
| 주차 마감 | `/weekly-close` → `/assess` (이해도 5수준 판정) |

에이전트 4종: `study-coach` · `code-reviewer` · `incident-analyst` · `concept-verifier`.

## 폴더

| 경로 | 언제 채우나 |
|---|---|
| `docs/weekly/` | 매주 (9절 템플릿 `_TEMPLATE.md`) |
| `labs/` | 1–6주 짧은 실습 |
| `llm-from-scratch/` | 7–9주 tokenizer·attention·transformer |
| `apps/api/` | 4주~ FastAPI |
| `apps/web/` | 11주~ Next.js |
| `packages/shared/` | 12주~ 공통 타입·스키마 |
| `evals/` | 21주~ 평가 데이터·스크립트 |
| `refs/notion/` | 로드맵 원문 (**수정 금지**) |

> 빈 폴더는 `.gitkeep` 만 있다. **미리 채우지 않는다** — 각 주차에 직접 만드는 것이 학습이다.

## 인코딩 규약 (두 PC 다 Windows)

| 확장자 | 인코딩 | 줄바꿈 |
|---|---|---|
| `.ps1` | UTF-8 **BOM 필수** | CRLF |
| `.sh` · `.githooks/*` | UTF-8 (BOM 금지) | LF |
| `.py` · `.md` · `.json` · `.ts` | UTF-8 (BOM 없음) | LF |

`.ps1` 에 BOM 이 없으면 Windows PowerShell 5.1 이 CP949 로 오해석해 **한글이 든 줄이
조용히 사라진다.** 반대로 `.sh` 에 BOM 이 붙으면 Git Bash 가 셔뱅을 못 읽는다.
`.gitattributes` 가 줄바꿈은 강제하지만 **BOM 은 강제하지 못하므로** 직접 챙겨야 한다.
