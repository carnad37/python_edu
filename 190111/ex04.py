#append는 리스트안에 요소 추가
a=[1,2,3]
a.append(4)
print(a)

a=[]
one=1
a.append(one)
a.append(2)
a.append(3)
a.append(4)
print(a)

#sort()리스트의 요소들을 정렬
#정순 (), 역순(reverse=True)를 넣어준다.
a=[1,4,3,2]
a.sort()
print(a)

a=['a','c','b']
a.sort(reverse=True)
print(a)

#reverse()는 요소들을 역순으로 뒤집는다. 걍 뒤집기만함.

a.reverse()
print(a)

#insert(위치,값)은 위치는 인덱스위치. 기존에 요소가 있는 위치일경우 이전요소는 한자리씩 밀려남.

a.insert(3,'d')
print(a)

#extend()는 여러개의 값을 추가 가능.

a=[1,2,3]
a.extend()

#index()는 리스트에서 찾으려는 값의 위치를 반환한다.
#index(찾으려는 요소의 값,탐색이 시작하는 위치, 탐색을 종료할 위치?)

a=[1,2,3,4,3,6]
loc=a.index(3)
print(loc)
print(a.index(1))
loc1=a.index(3,0)
print(loc1)

#count() 리스트 안에 요소의 갯수를 확인
#count(확인할 요소의 값)
#리턴값은 갯수다.

a=[1,2,3,1]
tno=a.count(1)
print(tno)

#pop()는 리스트의 요소를 꺼내오는 함수
#다만 꺼내온 요소는 리스트에서 삭제됨. 요게 중요. 기존에도 그냥 꺼내올 수는 있으나 삭제는 안됨.
#리턴값은 꺼내온 값.
#pop(꺼내올 인수의 위치)

#remove()는 리스틔의 요소를 제거
#remove(요소)

a=[1,2,3,5,4,3]
a.remove(3)
print(a)

#clear()는 리스트내의 모든 요소를 제거.

a.clear()
print(a)