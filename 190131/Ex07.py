#readlines()모든 라인을 읽어 저장

f = open("D:/hhs2/file/새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
