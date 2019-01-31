#hex(x)는 정수값을 받아 16진수로 변환하여 리턴해준다.(0x?? 식의 값이면 16진수)

retVal = hex(9)
print(retVal)
retVal = hex(10)
print(retVal)
retVal = hex(234)
print(retVal)

#oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 리턴하는 함수(0o?? 식의 값이면 8진수)

retVal = oct(34)
print(retVal)
retVal = oct(12345)
print(retVal)

#max(iterable)은 반복가능한 자료형을 입력받아 그 최대값을 리턴하는 함수

retVal = max([1,2,3])
print(retVal)
retVal = max("python") #문자열의 경우 아스키 코드값으로 비교됨.
print(retVal)

#min(iterable)은 맥스랑 반대.

retVal = min([1,2,3])
print(retVal)
retVal = min("python") #문자열의 경우 아스키 코드값으로 비교됨.
print(retVal)

#pow(x,y)는 x의 y제곱한 결과값을 리턴하는 함수

retVal = pow(2,4)
print(retVal)
retVal = pow(3,3)
print(retVal)
