#x=11
#y=2
#sum_01=x//y
#print(sum_01)

#//는 정수외에 버리는 나눗셈 연산자.

"""
i=7
j=4
result = i/j
print(result)
result = i//j
print(result)
result = i%j
print(result)

#**지수 연산자(몇 승)
#그외에는 자바랑 비슷비슷.
#
result = 10+20/2
print(int(result))
result =(10+20)/2
print(int(result))
"""
s=int(input("분자를 입력하시오: "))
m=int(input("부모를 입력하시오: "))
resultD=(s//m)
print("나눗셈의 몫 =",resultD)
resultN=(s%m)
print("나눗셈의 나머지 =",resultN)
