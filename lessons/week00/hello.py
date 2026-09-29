while True:
    name = input("이름: ").strip()
    if name:
        break
    print("이름을 입력하세요")

print(f"안녕하세요, {name}!")
