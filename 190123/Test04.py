def sub_Number(num01,num02):
    res = num01-num02
    print("preResult:",res)
    return res

num01 = int(input("첫번째 수를 입력해주세요: "))
num02 = int(input("두번째 수를 입력해주세요: "))

res = sub_Number(num01,num02)
print("postResult :",res)