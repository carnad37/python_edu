x=input("이름을 입력하시오: ")  #입력된 값은 문자열이다.
print(x,"씨, 안녕하세요?")
print("파이썬에 오신 것을 환영합니다.")
a=input("첫 번째 정수를 입력하시오: ")
b=input("두 번째 정수를 입력하시오: ")
a=int(a)   #input된 값은 문자열이다. int로 바꿔줘야 산술이 가능하다.
b=int(b)
sum=a+b     #출력때 산술하는것보다, 변수의 산술을 끝낸후 출력하는게 후에 수정 또는 확인하기 좋다.
print(a,"과",b,"의 합은",sum,"입니다.")