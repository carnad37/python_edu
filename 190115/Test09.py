years = int(input("나이를 입력해주세요: "))

if years > 60:
    print("노인")
elif years > 30:
    print("장년충")
elif years >= 19:
    print("젊은이")
elif years >= 8:
    if years >= 17:
        print("고등학생")
    elif years >= 14:
        print("중학생")
    else:
        print("초등학생")
else:
    print("어린이")