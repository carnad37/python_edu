icecream = {"탱크보이":1200,"폴라포":1200,"빵빠레":1800,"월드콘":1500,"메로나":1000}
New_product={'팥빙수':2700, '아맛나':1000}
New_product_keys =list(New_product.keys())
New_product_Vals =list(New_product.values())
#리스트로 변경->재조합?
for i in range(0,len(New_product_keys),1):
    icecream[New_product_keys[i]] = New_product_Vals[i]
print(icecream)





