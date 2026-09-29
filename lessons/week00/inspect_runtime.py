import os
import sys
from pathlib import Path

print("Python:", sys.executable) # 실제 실행 중인 Python의 위치
print("작업 폴더:", Path.cwd()) # 상대 경로를 해석하는 기준
print("소스 폴더:", Path(__file__).resolve().parent) 
print("프로세스 ID:", os.getpid()) # 실행마다 달라질 수 있는 번호

target = Path(__file__).resolve().parent / "practice.txt"
target.write_text("공부", encoding="utf-8") # 파일에 문자열을 기록
print("저장 위치:", target) # 저장된 파일의 위치
print("다시 읽기:", target.read_text(encoding="utf-8")) # 파일에서 문자열을 읽기