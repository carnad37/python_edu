#밑변 높이 입력.
#넓이 계산. Y나 y가 아닐시 종료

base = 0
height = 0
area = 0
checker = ""
while True:
    base = int(input("base = "))
    height = int(input("height = "))
    area = base*height/2
    print("Triangle width :",area)
    checker = input("Continue? ")

