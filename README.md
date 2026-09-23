# LLM_Study

LLM · Agentic AI 학습 저장소. 두 대의 PC(`RJH` / `RMS_Digital`)에서 공유한다.

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
`git pull` / `git checkout` 직후에는 훅이 자동으로 실행한다.

문제가 있으면 노란 글씨로 알려준다 — 등록되지 않은 PC, `.env` 없음, 필수 키 누락 등.
**절대경로를 코드나 문서에 직접 박지 않는다.** PC 의존 값은
`tools/study-config/study-config.json` 의 `hosts` 블록 한 곳에만 둔다.

## 폴더

| 경로 | 용도 |
|---|---|
| `notes/` | 학습 노트 |
| `labs/` | 실습 코드 |
| `refs/notion/` | Notion export 원문 |
| `refs/papers/` | 논문·자료 |
| `tools/study-config/` | PC 별 경로 해석 |
| `.claude/agents/` · `.claude/skills/` | Claude Code 에이전트·스킬 |

대용량(모델 가중치·데이터셋)은 저장소에 넣지 않는다. `hosts.<PC>.data_root`
(`RMS_Digital` 은 `D:/LLM_Data`)에 두고 경로만 맞춘다 — DF 저장소의
`Test/Data/PA55_NS_Data` 와 같은 방식이다.

## 인코딩 규약 (두 PC 가 다 Windows 라 반드시 지킬 것)

| 확장자 | 인코딩 | 줄바꿈 |
|---|---|---|
| `.ps1` | UTF-8 **BOM 필수** | CRLF |
| `.sh` | UTF-8 (BOM 금지) | LF |
| `.py` · `.md` · `.json` | UTF-8 (BOM 없음) | LF |

`.ps1` 에 BOM 이 없으면 Windows PowerShell 5.1 이 CP949 로 오해석해 **한글이 든
줄이 조용히 사라진다.** 반대로 `.sh` 에 BOM 이 붙으면 Git Bash 가 첫 줄을 못 읽는다.
`.gitattributes` 가 줄바꿈은 강제하지만 **BOM 은 강제하지 못하므로** 직접 챙겨야 한다.
