#zip(iterable)은 길이가 같은 반복 자료들을 같은 위치(인덱스)의 값끼리 튜플로 묶은 자료형을 리턴해주는 함수

retVal = list(zip([1,2,3], [4,5,6]))
print(retVal)
retVal = list(zip([1,2,3],[4,5,6],[7,8,9]))
print(retVal)
retVal = list(zip("abc","def"))
print(retVal)
