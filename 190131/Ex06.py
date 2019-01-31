#open(), close()로 파일을 열닫.

#readline()은 한줄씩 읽어옴
f=open("D:/hhs2/file/새파일.txt",'r')
line = f.readline()
print(line)
f.close()
print("")
f=open("D:/hhs2/file/새파일.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()