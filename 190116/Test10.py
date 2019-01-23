weight = int(input("몸무게를 입력해주세요: "))
tall = int(input("키를 입력해주세요: "))
obes = (weight+100)-tall
if obes>0:
    print(obes,"\nObesity")

print("\n"+"-"*30+"\n")