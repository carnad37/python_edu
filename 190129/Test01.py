#딕셔너리 구성
engTokor = {"one":"하나","two":"둘","three":"셋"}


while True:
    # 단어입력
    inputWord = input("단어를 입력하시오: ")
    if(inputWord == "q"):
        break
    #get으로 값 얻어오기
    searchMean = engTokor.get(inputWord)
    print(searchMean)

    #키값만 이용하기
    searchmean = engTokor[inputWord]
    print(searchMean)

