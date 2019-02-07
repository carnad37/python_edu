#test.txt에서 java라는 문자열을 python으로 바꿔서 저장.
#리스트로 변경
#리스트에서 찾아서
#변경 후 다시 입력
java = "java"
python = "python"

infile = open("D:/hhs2/file/test01.txt",'r')
lines = infile.readlines()
infile.close()
#line은 test문서를 행으로 묶어 리스트에 저장한것.
res_List = []
for i in lines:
    line = i.replace(java,python)
    res_List.append(line)
#res_List는 line을 서치해서 java를 찾아 모조리 python으로 바꿔버림.
outfile = open("D:/hhs2/file/test01.txt",'w')
for i in res_List:
    outfile.write(i)
outfile.close()

