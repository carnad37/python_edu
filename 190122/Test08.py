#이중 반복
#(n-1, n)으로 반복

i=1
num = int(input("정수를 입력해주세요: "))

while i<(num):
    for j in range(1,num+1,1):
        print("(%d, %d)"%(i,j),end=" ")
    print("")
    i+=1