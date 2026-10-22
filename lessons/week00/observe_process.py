import os
import time

payload = bytearray(8 * 1024 * 1024)  # 8 MiB의 바이트 데이터
# 일정 간격으로 값을 써서 실제 메모리 접근을 발생시킨다.
# 4096은 실험 간격이며 모든 PC의 페이지 크기를 주장하는 값은 아니다.
for offset in range(0, len(payload), 4096):
    payload[offset] = 1

print("PID:", os.getpid(), flush=True)
print("payload bytes:", len(payload), flush=True)
print("60초 동안 관찰합니다. 중단: Ctrl+C", flush=True)
time.sleep(60)
print("종료")