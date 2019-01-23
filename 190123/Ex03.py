def sum(a,b):
    tNum = 0
    for i in range(5):
        print("f1",i)
        if(i==4):
            return
        tNum = tNum+i
        print("f2",tNum)
    return tNum

x=2
y=4
ret = sum(2,4)
print("m1",ret)

#입력된 리턴 값이 없으면 None반환