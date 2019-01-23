def merge_string(str01,str02):
    res = str01+str02
    print("preResult :",res)
    return res

str1=input("문자를 입력해주세요: ")
str2=input("문자를 입력해주세요: ")

res = merge_string(str1,str2)
print("postResult :",res)