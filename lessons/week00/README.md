# Week 00 — 실행 환경 이해

## 목적
코드가 어디에 있고, 어떤 Python 이 실행하며, 실행 중 값과 실행 후 남는 값이 각각 어디에 있는지 직접 확인한다.

- 소스 파일(디스크) 과 실행 중 프로세스(RAM) 를 구분한다.
- **작업 폴더**(`Path.cwd()`)와 **소스 폴더**(`Path(__file__)`)가 다를 수 있음을 본다.
- 파일이 없을 때 `exists()` 와 `try/except` 가 어떻게 다른지 비교한다.

## 소스 파일

| 파일 | 하는 일 |
|---|---|
| `inspect_runtime.py` | 실행 중인 Python·작업 폴더·소스 폴더·프로세스 ID 를 출력하고, `practice.txt` 를 쓰고 다시 읽는다. `memo.txt` 유무를 `exists()` 로 확인한다(`try/except` 방식은 주석으로 보관). |
| `hello.py` | 이름을 입력받아 `strip()` 한 뒤, 비었으면 `이름을 입력하세요` 를 출력하고 다시 입력받는다(`while True` / `break`). 값이 있으면 f-string 으로 인사를 출력한다. |

`practice.txt` 와 `memo.txt` 는 실행 산출물·실험 파일이라 `.gitignore` 에 있다.

## 실행 방법
저장소 루트(`LLM_Study`)에서 실행한다. 경로가 루트 기준이라 다른 폴더에서는 `lessons/...` 를 찾지 못한다.

```powershell
python lessons/week00/inspect_runtime.py
python lessons/week00/hello.py
```

가상환경 Python 으로 실행하려면 (활성화 없이):

```powershell
.\.venv\Scripts\python.exe lessons/week00/inspect_runtime.py
```

## 입출력 예시 (`hello.py`)

| 입력 | 출력 |
|---|---|
| `재학` | `안녕하세요, 재학!` |
| 빈 입력 | `이름을 입력하세요` 를 출력하고 다시 입력을 기다린다 |
| 공백만 입력 | 같은 메시지, 다시 입력을 기다린다 |
| 빈 입력 → 공백만 → `재학` | 메시지 두 번 뒤 `안녕하세요, 재학!` |
| `  재학  ` (앞뒤 공백) | `안녕하세요, 재학!` (공백 없이) |
| 입력 스트림이 끝남 (EOF) | `EOFError: EOF when reading a line` 로 종료 (아직 처리하지 않음) |

## 검증 결과

- [x] 정상 입력 — `hello.py` 를 파이프 입력으로 실행해 확인
- [x] 빈 입력·공백만 입력 (다시 입력받음) — 파이프 입력으로 확인. 개선 전에는 `ValueError` 로 종료했다
- [x] 입력 스트림이 끝나는 경우 — `EOFError` 로 종료됨을 확인(처리는 안 함)
- [x] 작업 폴더를 바꿔 다시 실행 — 작업 폴더만 달라지고 소스 폴더·저장 위치는 같았다
- [x] 시스템 Python 과 venv Python 비교 — `Python:` 줄만 달랐다
- [x] `exists()` 와 `try/except` 비교 — 본인이 직접 실행해 두 방식 모두 정상 동작을 확인(출력은 첨부하지 않음)

## 콘솔 로그

저장소 루트에서 `python lessons/week00/inspect_runtime.py`:

```text
Python: C:\Python314\python.exe
작업 폴더: C:\Users\RJH\Desktop\LLM_Study
소스 폴더: C:\Users\RJH\Desktop\LLM_Study\lessons\week00
프로세스 ID: 32752
메모: exit company
저장 위치: C:\Users\RJH\Desktop\LLM_Study\lessons\week00\practice.txt
다시 읽기: 공부
```

`lessons/week00` 에서 `python inspect_runtime.py`:

```text
Python: C:\Python314\python.exe
작업 폴더: C:\Users\RJH\Desktop\LLM_Study\lessons\week00
소스 폴더: C:\Users\RJH\Desktop\LLM_Study\lessons\week00
프로세스 ID: 22076
메모: exit company
저장 위치: C:\Users\RJH\Desktop\LLM_Study\lessons\week00\practice.txt
다시 읽기: 공부
```

venv Python 으로 실행했을 때 첫 두 줄:

```text
Python: C:\Users\RJH\Desktop\LLM_Study\.venv\Scripts\python.exe
작업 폴더: C:\Users\RJH\Desktop\LLM_Study
```

- 프로세스 ID 는 실행마다 다르다(32752, 22076).
- 작업 폴더만 바뀌고 소스 폴더와 `practice.txt` 위치는 그대로다. 경로를 `__file__` 기준으로 만들었기 때문이다.

`python lessons/week00/hello.py` (파이프로 `빈 줄`, `공백만`, `재학` 순서로 입력):

```text
이름: 이름을 입력하세요
이름: 이름을 입력하세요
이름: 안녕하세요, 재학!
```

파이프 입력이라 프롬프트 뒤에 출력이 같은 줄에 붙어 보인다. 직접 실행하면 줄이 나뉜다.

입력 스트림이 끝난 경우(마지막 줄):

```text
EOFError: EOF when reading a line
```

## 한계와 다음 개선 1개

**한계**
- `exists()` 의 틈(확인 직후, 읽기 전에 다른 프로세스가 파일을 지우는 경우)은 재현하지 못했다. `try/except` 가 더 안전하다는 결론은 개념에서 나온 것이지 이 실험이 증명한 것이 아니다.
- `hello.py` 는 이름의 내용을 검증하지 않는다. `strip()` 뒤 비어 있지만 않으면 숫자나 특수문자만 있어도 통과한다.
- `input()` 은 항상 문자열이다. `10` 을 입력해도 숫자가 아니라 `"10"` 이다.
- `hello.py` 는 입력이 끊기면(EOF, 파이프 종료, `Ctrl + Z`) `EOFError` 로 멈춘다. 재입력 루프가 이 경우를 처리하지 않는다.
- `hello.py` 로그는 파이프 입력 기준이라, 직접 실행할 때와 프롬프트 줄바꿈이 다르게 보일 수 있다. 직접 키보드로 입력해 확인한 로그는 아니다.
- `memo.txt` 는 UTF-8 이라고 가정했다. 다른 인코딩이면 `UnicodeDecodeError` 가 나고, 이 오류는 `except FileNotFoundError` 로 잡히지 않는다.

**다음 개선 1개**
- `hello.py` 에서 `EOFError` 를 `except EOFError:` 로 잡아 안내 메시지를 출력하고 종료한다. 예외 종류를 구체적으로 적어, 다른 오류까지 삼키지 않게 한다.
- 이미 반영한 개선: 빈 입력이면 예외 대신 다시 입력받게 바꿨고(`while`), f-string 비교용 실험 줄은 지웠다.
