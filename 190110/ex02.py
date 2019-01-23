# %d로 실수 대입가능
str="I eat %d apples."%3
print(str)
#실사용할땐 변수들만 이용
num=3
str="I eat %d apples."
fStr=str%num
print("\n"+fStr)
# %d로 변수를 문자열에 대입가능
str="I eat %s apples."%"five"
print("\n"+str)
#역시 실사용시에는 변수들로 대체
str1="five"
str="I dat %s apples."
fStr=str%str1
print("\n"+fStr)
#여러개일시엔 아래와 같이 한다
str="I eat %d apples and %d oranges"%(3,4)
print("\n"+str)
#이거역시 가능하넹.
str="I eat %d apples and %d oranges"
num1=3
num2=4
fStr=str%(num1,num2)
print("\n"+fStr)