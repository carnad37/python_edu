#다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상의 점수들의 총합을 구하시오.
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

count = 0
sum = 0
stuNum = 0
lenA = len(A)
while count < len(A):
    res = A[count]
    if(res >= 50):
        sum = sum + res
        #stuNum = stuNum + 1
    count = count + 1
print("학생들의 점수의 합은",sum,"이다.")
"""
sum = 0
count = 0
#미리 A를 선별하는 방법도 있다. if문을 통해 다른 리스트로 50이상값만 옮김.
#while count < len(A):
#    if(A[count] > 50)
#    count = count + 1

#A를 점수순으로 나열, 50이후의 요소만 계산하는 법도 있다.

A.sort()
"""



