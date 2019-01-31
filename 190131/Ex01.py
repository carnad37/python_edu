#abs(x)는 어떤값을 입력받을시 절대값을 돌려줌

absVal = abs(3)
print(absVal)
absValsVal = abs(-3)
print(absVal)
absVal = abs(-1.2)
print(absVal)

#all(x)는 반복가능한 자료형(리스트,튜플, 딕셔너리, 문자열 etc의 for문으로 출력가능한것) x를 입력받아서,
#x의 요소중에 하나로도 거짓이있으면 False를 리턴한다.

retVal = all([1,2,3])
print(retVal)
retVal = all([1,2,3,0]) #0이 거짓
print(retVal)

#any(x)는 반복가능한 자료형(리스트,튜플, 딕셔너리, 문자열 etc의 for문으로 출력가능한것) x를 입력받아서,
#x의 요소중에 하나로도 참이있으면 True를 리턴한다.

retVal = any([1,2,3,0])
print(retVal)
retVal = any([0,""])
print(retVal)

#chr(val)는 아스키코드값을 입력받아서 대응하는 문자를 리턴해주는 함수이다.

retVal = chr(97)
print(retVal)
retVal = chr(48)
print(retVal)

#ord(c)는 문자의 아스키코드값을 리턴하는 함수이다.

retVal = ord('a')
print(retVal)
retVal = ord('0')
print(retVal)