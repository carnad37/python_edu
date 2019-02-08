infile = open("d:\\hhs2\\file\\sample.txt",'r')
num_List = []
for line in infile:
    line = int(line.strip("\n"))
    num_List.append(line)
num_Sum = sum(num_List)
count = len(num_List)
avg = num_Sum/count
infile.close()

outfile = open("d:\\hhs2\\file\\result.txt",'w')
outfile.write("총합 : %d\n평균 : %d"%(num_Sum,avg))
outfile.close()