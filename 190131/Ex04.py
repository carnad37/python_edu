#round(number[,ndigits])는 숫자를 입력받아 반올림해주는 함수.
#ndigits는 소수점의 자리수

retVal = round(4.6)
print(retVal)
retVal = round(4.2)
print(retVal)
retVal = round(5.678,2)
print(retVal)

#sorted()는 본래 자료를 변화시키지 않고 변화된 리턴값(iterable)를 보내주는 함수.
#sort()는 본래 자료 자체를 변형시켜주는 함수

retVal = sorted(['a','c','b'])
print(retVal)
retVal = sorted("zero")
print(retVal)
retVal = sorted((3,2,1))
print(retVal)


numList = [3,1,2]
retVal = sorted(numList)
print(retVal)
print('sorted() numList:',numList)
retVal = numList.sort()
print(retVal)
print('sort() numList:',retVal)

#sum(iterable)은 입력받은 자료의 값들을 모두 합하여 리턴해주는 함수

retVal = sum([1,2,3])
print(retVal)
retVal = sum((4,5,6))
print(retVal)
