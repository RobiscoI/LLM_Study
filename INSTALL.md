# 이 팩을 LLM_Study 에 넣는 법

이 zip 은 **기존 `LLM_Study` 저장소에 덮어 넣는 추가 파일**이다. 기존 README·.gitignore·.env.example·requirements-dev.txt·labs·tools·.githooks 는 건드리지 않는다.

1. zip 을 풀어 나온 파일을 `LLM_Study` 루트에 그대로 복사한다 (같은 이름 파일이 있으면: `docs/` 아래만 겹칠 수 있다 → 기존 파일을 열어 보고 합친다).
2. `.gitignore` 에 아래 한 줄이 없으면 추가한다:
   ```
   .claude/settings.local.json
   ```
3. PowerShell(프로젝트 루트)에서:
   ```powershell
   npm install -g @anthropic-ai/claude-code    # Node v24 이미 있음
   claude                                       # 첫 실행 시 로그인(개인 Pro), Context7 MCP 승인
   /weekly-start
   ```
4. 코치가 "git pull 하셨나요?" 로 시작하면 성공. `/agents` 로 4개 에이전트, `/help` 로 5개 스킬이 보이는지 확인.
5. 커밋: `git add -A` → `git commit -m "week-01: Claude Code 코치 설정 추가"` → `git push`

들어 있는 것
- `CLAUDE.md` — 코치 지침 정본 (Notion 의 GPT 지침을 옮기고 현재 PC 환경을 반영)
- `.claude/settings.json`, `.claude/hooks/after_edit.py` — 권한·차단 목록, .py 자동 문법 검사
- `.claude/agents/` — reviewer · debugger · test-writer · retro-writer
- `.claude/skills/` — /weekly-start /explain-concept /code-review /debug-trace /weekly-retro
- `.mcp.json` — Context7 (라이브러리 공식 문서)
- `docs/progress.md` (10-13 상태 반영) · `environment.md` (실측값 반영) · `commands.md` · `decision-log.md` · `weeks/TEMPLATE.md` · `errors/TEMPLATE.md` · `glossary/README.md`
- `scripts/new_week.py` — `lessons/weekNN` + `docs/weeks/week-NN.md` 생성
