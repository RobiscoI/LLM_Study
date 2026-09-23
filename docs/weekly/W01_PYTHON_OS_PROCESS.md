# 1주차 · Python·OS·프로세스

## 이번 주 결과

- [x] Git 저장소와 로드맵 디렉터리 확인
- [x] 파일 기반 CLI 메모 앱 구현
- [x] 정상·경계·실패 테스트 7개 작성
- [ ] 로컬 Python 설치 및 `.venv` 생성
- [ ] 로컬에서 테스트 재실행
- [ ] 오류 하나를 원인 → 가설 → 검증 순서로 기록

## 핵심 질문

1. 소스 파일과 실행 중인 프로세스는 무엇이 다른가?
2. 현재 작업 디렉터리가 상대 경로에 영향을 주는 이유는 무엇인가?
3. 가상환경은 어떤 Python과 패키지를 격리하는가?

## 환경 확인

현재 확인 결과 Git은 설치되어 있으나 시스템 PATH에서 `python`과 `py`를 찾지 못했다. Python 설치 후 **새 PowerShell**에서 다음 결과를 이 문서에 붙인다.

```powershell
git --version
python --version
where.exe python
python -c "import os, sys; print(sys.executable); print(sys.prefix); print(os.getcwd())"
```

## 구현 선택

- 핵심 로직과 CLI를 분리해 파일이나 subprocess 없이 규칙을 테스트한다.
- JSON을 읽은 직후 구조를 검증해 손상된 데이터를 조용히 덮어쓰지 않는다.
- UTF-8과 `ensure_ascii=False`로 한글을 사람이 읽을 수 있게 저장한다.
- 임시 파일 작성 후 교체해 저장 도중 기존 데이터가 잘릴 위험을 줄인다.
- 예상 가능한 사용자 오류는 메시지와 종료 코드 `1`로 전달한다.

## 실행 및 검증

```powershell
python -m unittest labs.week01_notes.test_notes -v
python -m labs.week01_notes.cli --db work/week01-notes.json add "첫 메모"
python -m labs.week01_notes.cli --db work/week01-notes.json list
```

## 완료 판정

새 터미널에서 README만 보고 앱과 테스트를 실행하고, 손상된 JSON을 넣었을 때 원인을 설명하는 오류가 출력되면 완료다.
