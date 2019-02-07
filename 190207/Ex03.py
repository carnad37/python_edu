#키보드로부터 입력된 내용을 계속 추가.
infile = open("d:\\hhs2\\file\\Test.txt",'a')
text = input("내용을 입력해주세요: ")
infile.write(text)
infile.write("\n")
infile.close()