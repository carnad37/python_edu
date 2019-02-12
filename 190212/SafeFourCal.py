class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def div(self):
        result = self.first / self.second
        return result
    def setdata(self,first,second):
        self.first = first
        self.second = second

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

cal1 = SafeFourCal(4,0)
ret = cal1.div()
print(ret)
cal1.setdata(4,2)
ret = cal1.div()
print(ret)