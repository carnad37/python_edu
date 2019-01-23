weight=float(input("몸무게를 입력해주세요: "))

if weight > 88.45:
    grade = "Heavy weight"
elif weight > 72.57:
    grade = "Cruiserweight"
elif weight > 61.23:
    grade = "Middleweight"
elif weight > 50.80:
    grade = "Lightweight"
else:
    grade = "Flyweight"

print(grade)
