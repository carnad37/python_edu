f=open("D:/hhs2/file/새파일.txt",'r')
while True:
    line = f.readline()
    print(line, "길이-",end="")
    print(len(line))
    if not line:break
f.close()
