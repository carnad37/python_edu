# inventory1 = {"메로나":300, "비비빅":400, "죠스바":250}
# inventory2 = {"메로나":20, "비비빅":3, "죠스바":100}
#
# name = "메로나"
# #1에서 메로나 가격 출력
# goods01 = inventory1[name]
# print(goods01,"원")
#
# #2에서 메로나 재고 출력
# goods02 = inventory2.get(name)
# print(goods02,"개")
#

inventory = {"메로나":[300,20], "비비빅":[400,3], "죠스바":[250,100]}
iKey = "메로나"
resList = inventory[iKey]
value = resList[0]
print(value)