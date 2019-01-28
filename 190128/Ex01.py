#튜블이란?
#리스트와의 차이는 값을 바꿀수 없다는 점이다.
#리스트 []로 출력, 튜플 ()로 출력된다.

t1 = (1,2,'a','b')
# del t1[0]
#를 출력시에 오류가 뜬다.
#TypeError: 'tuple' object doesn't support item deletion

i = t1[0]
j = t1[3]
print(i,j)

k =t1[1:]
print(k)
#값을 변경할수 없다는점 외에는 리스트와 같다.