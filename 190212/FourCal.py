class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first+self.second
        return result
    #파이썬에서 클래스내의 메소드를 만들시에 첫번째 인수로 self가 반드시 들어가야 한다.

# cal1 = FourCal()
# cal2 = FourCal()
#
# cal1.setdata(4,2)
# cal2.setdata(3,7)
#
# print(cal1.first)
# print(cal2.first)

cal3 = FourCal(5,7)
cal4 = FourCal(6,9)

ret = cal3.sum()
print(ret)
ret = cal4.sum()
print(ret)