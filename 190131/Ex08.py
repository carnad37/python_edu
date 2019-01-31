#read()는 전체를 읽어 문자열로 저장한다.(\n도 전부 포함)

f=open("D:/hhs2/file/새파일.txt",'r')
data = f.read()
print(data)
f.close()