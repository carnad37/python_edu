grade = input("등급을 입력해주세요(알파벳): ")
grade = grade.upper()

if grade == "A":
    print("Excellent")
elif grade == "B":
    print("Good")
elif grade == "C":
    print("Usually")
elif grade == "D":
    print("Effort")
elif grade == "F":
    print("Failure")
else:
    print("error")

