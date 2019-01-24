def calculate_area(radius):
    global area #전역변수라고 선언하여 전역변수에 영향을 준다.(선언하지 않을시, return값이 없기때문에 area는 리턴되지않는다)
    area = 3.14*radius**2
    return

area = 0
r = float(input("원의 반지름: "))
calculate_area(r)
print(area)