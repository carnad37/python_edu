age = int(input("나이를 입력해주세요: "))
if age>=20:
    print("adult")
else:
    age = 20-age
    print(age,"years later")