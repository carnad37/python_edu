#함수 만들기
"""
def print_address():
    print("서울특별시 종로구 1번지")
    print("파이썬 빌딩 7층")
    print("홍길동")

print_address()
"""
def print_address(name):
    print("서울특별시 종로구 1번지")
    print("파이썬 빌딩 7층")
    print(name)

print_address("홍길동")

def upperNumber(num):
    num = num*10
    cut = int(num)*10
    num = int(num*10)
    res = num - cut
    if(res>=5):
        cut+=10
    cut = cut/100
    return cut

x= 66.6666666
y = upperNumber(x)
print(y)