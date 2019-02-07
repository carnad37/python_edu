
infile = open("D:/hhs2/file/proverbs.txt",'r')
for line in infile:
    print(line)
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word)
infile.close()