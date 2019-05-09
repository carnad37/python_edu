#dir은 객체가 자체적으로 가지고있는 변수나 함수를 보여준다.

retVal = dir([1,2,3])
print(retVal)
retVal = dir({'1':'a'})
print(retVal)

#divmod(a,b)는 2개의 숫자를 입력으로 받는다. a를 b로 나눠 (몫, 나머지)를 튜플형으로 리턴해주는 함수이다.

retVal = divmod(7,3)
print(retVal)

#iterator를 입력받아 인덱스 값을 포함하는 enumerate객체를 리턴해준다.
for i, name in enumerate(['body','foo','bar']):
    print(i,name)

#eval(expression)은 실행가능한 문자열을 입력받아 문자열을 실행한 결과값을 리턴.
#수는 물론이거니와, 문자열 함수등도 가능....ㄷ
retVal = eval('1+2')
print(retVal)
retVal = eval("'hi'+'a'")
print(retVal)
retVal = eval('divmod(4,3)')
print(retVal)


#filter함수는 (함수이름, 대상)으로 대상값들을 하나씩 함수에 대입해 참인경우만 리턴해준다.
#즉 대상이 되는 함수역시 불값만 리턴되는 함수여야 한다.
val = [1,-3,2,0,-5,6]
def positive(x):
    result = []
    for i in x:
        if i>0:
            result.append(i)
    return result
retVal = positive(val)
print(retVal)

def siPositive(x):
    return x > 0
retVal = list(filter(siPositive,val))
print(retVal)
