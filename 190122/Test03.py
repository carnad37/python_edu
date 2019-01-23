#10개 입력. 짝수와 홀수의 갯수 출력.
even = 0
odd = 0
for i in range(1,11,1):
    num = int(input("%d번째 정수를 입력해주세요: "%i))
    #짝수인지 홀수인지 판단
    if(num%2==0):
        odd += 1
    else:
        even += 1
print("even : %d"%even)
print("odd : %d"%odd)
