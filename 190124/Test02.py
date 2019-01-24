#원의 넓이를 입력받아 반지름을 리턴하는 함수]
import math

def convert_radius(area):
    #area는 r제곱*파이다
    #입력받은 area를 파이로 나눠주고 루트를 씌운다.
    area = area/3.14
    result = math.sqrt(area)
    return result

#원의 넓이를 입력
area = float(input("원의 넓이를 입력해주세요: "))
r = convert_radius(area)
print(r)