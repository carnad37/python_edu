infile = open("d:\\hhs2\\file\\abc.txt",'r')
sum_List = []

while True:
    line = infile.readline()
    line = line.strip('\n')
    #양쪽의 빈칸이나 띄어쓰기 넘기기 등등 빈칸을 모조리 컷해줌.
    if not line: break
    #
    sum_List.append(line)
infile.close()
#sum_List에 각각의 행을 저장함. \n은 제거.

sum_List.reverse()

outfile = open("d:\\hhs2\\file\\abc.txt",'w')
for i in sum_List:
    outfile.write(i)
    outfile.write('\n')
    #위에서 제거한 \n을 입력할때마다 추가해주기.
outfile.close()
