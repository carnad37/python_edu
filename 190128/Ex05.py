a = {'name' : 'pey','phone':'0119993323','birth':'1118'}
aKeys = a.keys()
print(aKeys)

#dict_keys(['name', 'phone', 'birth'])
#로 출력되게 되는데, dict_keys는 리스트처럼 사용이 가능한 또 하나의 자료형이다.

for kVal in aKeys:
    print(kVal)

print(type(aKeys))

alist=list(aKeys)
print(alist)
#list()를 통해서 아예 리스트가된다.