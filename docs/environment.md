# 환경 기록

설치할 때마다 한 줄씩 추가한다. "설치 완료" 판정은 로드맵의 6단계(공식 문서 확인 → 설치 → 새 터미널 → 검증 → 최소 실행 → 실패 기록)를 거친 뒤에만.
아래 값은 Notion 메인 페이지 "USER PC 설치 현황"(2026-10-13 실측, 10-14 Docker 추가)을 옮긴 것이다. 다른 PC는 행을 추가한다.

## 기기

| 이름 | OS | 사양 | 용도 |
|---|---|---|---|
| USER PC | Windows 11 Pro 10.0.26200 | i7-12650H · RAM 15.7GB · RTX 4050 Laptop 6GB · C: 여유 약 337GB | 주 학습 |
| (회사 PC) | | | |
| (노트북) | | | |

## 도구 (USER PC)

| 장 | 도구 | 버전 | 경로 / 확인 명령 | 상태 |
|---|---|---|---|---|
| 0 | Python | 3.14.4 | `C:\Python314\python.exe` · `where.exe python` | 기존 |
| 0 | Git | 2.54.0.windows.1 | `git --version` | 기존 |
| 0 | VS Code | 1.141.0 (Python·Pylance 확장) | `code --version` | 기존 |
| 0 | 저장소 `LLM_Study` | — | `Desktop\LLM_Study` · 훅 `.githooks` · `.env`는 예시 복사본 | 준비됨 |
| 0~1 | `.venv` | Python 3.14.4 | pytest 9.1.1 · ruff 0.17.0 · anthropic 1.13.0 · python-dotenv 1.2.4 | 준비됨 |
| 0 | Claude Code | | `claude --version` | **설치 필요** (`npm install -g @anthropic-ai/claude-code`) |
| 9 | Ollama | 0.40.3 | `%LOCALAPPDATA%\Programs\Ollama` · `127.0.0.1:11434` | 설치됨 |
| 9 | 로컬 모델 | qwen2.5:0.5b (Q4_K_M, 397MB) | `ollama list` | 받음 |
| 12 | Node.js LTS | v24.15.0 · npm 11.12.1 | `node --version` | 기존 |
| 14 | SQLite | 3.50.4 | `import sqlite3` | Python 내장 |
| 14 (선택) | Docker Desktop | 4.95.0 · Engine 29.8.2 · Compose v5.6.0 | `docker run --rm hello-world` | 설치됨, **재부팅 후 재확인 필요** |
| 14 (선택) | PostgreSQL | — | 14장 선택 경로에서 Docker 컨테이너로 | 미설치 |
| 23 (선택) | gh CLI | 2.102.0 | `gh auth status` | 로그인 안 됨 |
| 4~20 | 주차별 패키지 | fastapi 0.143 · numpy 2.5 · torch 2.14 · mcp 2.3 · sqlalchemy 2.1 · psycopg 3.3 | `pip install --dry-run`으로 Python 3.14 휠 확인만 | 해당 장에 설치 |

## 남은 일 (0장 기록에서)
- `tools/study-config/study-config.json`의 `hosts`에 `USER` 항목 추가
- Docker Desktop 재부팅 후 `docker version` 재확인
- Ollama 첫 호출 153초(모델 로딩 62초) — 여유 RAM 200MB 상황이었음. 다른 프로그램 닫고 재측정
