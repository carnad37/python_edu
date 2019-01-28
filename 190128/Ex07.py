a = {'name' : 'pey','phone':'0119993323','birth':'1118'}

aItem = a.items()
print(aItem)
#키와 값을 튜플로 묶어서 출력.

alist = list(aItem)
print(alist)
#리스트로 바꿔줘도 튜플내의 값을 수정하는것은 불가능하다.

a.clear()
print(a)
#clear는 모조리 청소해버린다. 리스트때와 같다.