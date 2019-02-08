#리스트로 바꿔준다.
#if문을 통해 10개 이하 단어 카운트.

def word_toList(url):
    openfile = open(url,'r')
    word_List = []
    for line in openfile:
        line = line.strip("\n")
        word_List.append(line)
    openfile.close()
    return word_List
#10개 이하의 단어를 카운트해주는 함수
def count_wordList(word_List):
    count = 0
    for i in word_List:
        len_check = len(i)
        if(len_check<=10):
            count+=1
    return count


openfile = "d:\\hhs2\\file\\word.txt"
wList = word_toList(openfile)
ten_Word = count_wordList(wList)
print("10자 이하의 단어는 %d개 이다."%ten_Word)

