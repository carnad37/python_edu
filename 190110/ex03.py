#함수를 등록할때는 def로 시작한다.
def sum(a,b):
    s = a+b
    return s
total = sum(4,7)
print(total)

#보통은 파이썬에 이미 저장된 함수들을 사용한다.
#len()는 문자열의 길이를 세어주는 함수이다.
#좀다가 짝퉁 len만들어보장

print(type("안녕하세요"))
print(type(len("안녕하세요")))

#<class 'str'또는 'int'>같이 결과값이 나온다.

s="AbCdEfG"
#upper()는 대문자 변환 함수
su=s.upper()
#lower()는 소문자 변환 함수
sl=s.lower()
print(su)
print(sl)

#count()는 문자열내에 부분 물자열의 갯수를 파악해준다.
str="i am boy boy girl"
bNum=str.count("boy")
gNum=str.count("girl")
nNum=str.count("baby")
print(bNum,gNum,nNum)

#find()는 있는지 없는지 찾아줌. 찾으면 대상의 부분 문자열 인덱스값을 리턴. 못찾으면 -1.
#중복되는 문자열이 있어도 가장 첫번째 문자열만 나온다.
str="i am boy girl"
bNum=str.find("boy")
gNum=str.find("girl")
nNum=str.find("baby")
print(bNum,gNum,nNum)

#replace()는 새로운 문자열로 교환한다.
#replace(교환 대상, 교환하려는 대상)
str="i am boy."
wtf=str.replace("boy","girl")
print(wtf)

#join() '원본문자열.join()'이 아니라 '넣고싶은 문자열.join()'이다.
#또 join()은 문자 사이사이 마다 넣어주는것. 원하는 위치는 지정불가능하다.
ic=","
str="abcd"
insertedStr=ic.join(str)
print("원본 문자열:",str)
print("변경된 문자열:",insertedStr)

#잊지말기.
#int(),str(),float()다 함수인 것이다.
#java의 Integer.parseInt()같은 것.

str="Pithon"
n="y"
#nstr=str.replace("i",n)
#또는,
str1=str[:1]
str2=str[2:]
nstr=str1+n+str2

print(nstr)