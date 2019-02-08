def num_toList(url):
    openfile = open(url,'r')
    num_List = []
    for line in openfile:
        line = int(line.strip("\n"))
        num_List.append(line)
    openfile.close()
    return num_List

def cal_Avg(cal_List):
    n_Sum = 0
    counter = 0
    for i in cal_List:
        n_Sum += i
        counter += 1
    n_Avg = n_Sum/counter
    return (n_Sum, n_Avg)

def writeDate(url,nSum,nAvg):
    outfile = open(url,'w')
    outfile.write("총합 : %d\n평균 : %d"%(nSum,nAvg))
    outfile.close()

openUrl = "d:\\hhs2\\file\\sample.txt"
closeUrl = "d:\\hhs2\\file\\result.txt"
nSum = 0
nAvg = 0
num_List = num_toList(openUrl)
(nSum, nAvg) = cal_Avg(num_List)
writeDate(closeUrl,nSum,nAvg)