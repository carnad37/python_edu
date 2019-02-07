infile = open("d:\\hhs2\\file\\sample.txt",'r')
outfile = open("d:\\hhs2\\file\\result.txt",'w')
sum = 0
counter = 0

while True:
    line = infile.readline()
    line = line.strip()
    print(line)
    if not line: break
    num = int(line)
    sum += num
    counter += 1

avg = sum/counter
outfile.write("%d"%avg)

infile.close()
outfile.close()