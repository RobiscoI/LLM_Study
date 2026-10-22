# 명령 기록

성공한 명령과 **실패한 명령을 같이** 적는다. 실패 명령은 왜 실패했는지 한 줄. 기준 셸은 프로젝트 루트의 PowerShell.

| 날짜 | 장 | 명령 | 결과 | 비고 |
|---|---|---|---|---|
| 2026-10-13 | 0 | `.venv\Scripts\python.exe -m pytest -q labs/week01_notes` | 7 passed | 가상환경 직접 경로 사용 |
| | | | | |

## 자주 쓰는 명령 (PowerShell, 프로젝트 루트에서)

```powershell
# 가상환경 — 활성화가 안 되면 직접 경로로
.venv\Scripts\Activate.ps1          # 실행 정책 오류 시: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.venv\Scripts\python.exe -c "import sys; print(sys.executable)"

# 테스트
python -m pytest -q
python -m pytest -q lessons/week02

# 새 장 시작
python scripts/new_week.py 02 "자료구조와 알고리즘"

# Git 기본 3개
git add -A
git commit -m "week-02: ..."
git push

# Git 되돌리기 (안전한 방법)
git log --oneline -5
git revert <커밋id>

# Ollama
ollama list
ollama ps

# Claude Code
claude
/weekly-start
/weekly-retro
```
