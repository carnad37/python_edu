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

class MoreCal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result

cal1 = MoreCal(4,2)
ret = cal1.sum()
print(ret)
ret = cal1.pow()
print(ret)