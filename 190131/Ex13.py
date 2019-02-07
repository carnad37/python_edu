#write는 적어주는 기능. 'w'는 덮어쓴다.
outfile = open("d:\\hhs2\\file\\phones1.txt",'w')
outfile.write("홍길동 010-1234-5678\n")
outfile.write("김철수 010-1234-5679\n")
outfile.write("김영희 010-1234-5680\n")
outfile.close()