icecream = {"탱크보이":1200,"폴라포":1200,"빵빠레":1800,"월드콘":1500,"메로나":1000}

ice_KeyList = list(icecream.keys())
print(ice_KeyList)

ice_ValList = list(icecream.values())
print(ice_ValList)

income = sum(ice_ValList)
print(income)
#또는
income = 0
for i in range(0,len(ice_ValList),1):
    income+=ice_ValList[i]
print(income)
