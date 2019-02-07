infilemane = input("입력 파일 이름: ")
outfilename = input("출력 파일 이름: ")

infile = open("d:\\hhs2\\file\\%s.txt"%infilemane,"r")
outfile = open("d:\\hhs2\\file\\%s.txt"%outfilename,"w")

s = infile.read()

outfile.write(s)

infile.close()
outfile.close()
