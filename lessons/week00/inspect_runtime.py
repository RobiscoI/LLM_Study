import os
import sys
from pathlib import Path

print("Python:", sys.executable) # 실제 실행 중인 Python의 위치
print("작업 폴더:", Path.cwd()) # 상대 경로를 해석하는 기준
print("소스 폴더:", Path(__file__).resolve().parent) 
print("프로세스 ID:", os.getpid()) # 실행마다 달라질 수 있는 번호
print("prefix:", sys.prefix) # 지금 쓰는 환경의 루트 (venv 면 .venv)
print("base_prefix:", sys.base_prefix) # venv 를 만든 원래 Python 의 루트

memo = Path(__file__).resolve().parent / "memo.txt" # 경로 객체만 만든다. 파일은 만들어지지 않는다
if memo.exists():
    print("메모:", memo.read_text(encoding="utf-8")) # 파일에서 문자열을 읽기
else:
    print("메모 파일이 존재하지 않습니다.")

# try:
#    print(memo.read_text(encoding="utf-8"))
# except FileNotFoundError:
#    print("메모 파일이 존재하지 않습니다.")

target = Path(__file__).resolve().parent / "practice.txt"
target.write_text("공부", encoding="utf-8") # 파일에 문자열을 기록
print("저장 위치:", target) # 저장된 파일의 위치
print("다시 읽기:", target.read_text(encoding="utf-8")) # 파일에서 문자열을 읽기