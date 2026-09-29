name = input("이름: ").strip()
if not name:
    raise ValueError("이름은 비어 있을 수 없습니다")

print("안녕하세요, {name}!")
print(f"안녕하세요, {name}!")