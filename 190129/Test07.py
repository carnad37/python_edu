#총 3가지 메뉴.
#로그인을 했을때만 2,3 가능.
#1,2,3이 아닐 시엔 다시 입력.

#함수제작
#매개변수로 id를 전달해서 id가 존재하는지 리턴하는 함수 작성
#있을시엔 1을 리턴. 없을 시엔 0을 리턴.
#매개변수로 id를 전달해서 pw가 맞는지 리턴하는 함수 작성
#매개변수로 id를 전달해서 pw가 맞는지 리턴하는 함수 작성

def idChecker(id,pw):
    global user_id_List
    global user_pw_List
    check_res = 0
    #check_res가 0일시 id가 없다.
    #check_res가 1일시 id는 있는데 비밀번호가 없다.
    #check_res가 2일시 로그인가능.
    for i in range(0,len(user_id_List),1):
        if(id == user_id_List[i]):
            check_res = 1
            break
    if(check_res == 1):
        for i in range(0,len(user_pw_List),1):
            if(pw == user_pw_List[i]):
                check_res = 2
                break
    return check_res

def loginChecker(id):
    global login
    check = login[id]
    if(check):
        print(id+"님은 로그인 중입니다.")
    else:
        print(id+"님은 로그아웃 상태입니다.")


#1~3까지의 숫자만 입력가능.

#id, password 데이터
user = {"apple":"orange","chair":"desk","mouse":"keyboard","person":"pocket"}
user_id_List = list(user.keys())
user_pw_List = list(user.values())
login = {}
for i in range(0,len(user_id_List),1):
    login[user_id_List[i]]=False

while True:
    # 메뉴제작
    print("1. 로그인")
    print("2. 사용자 로그인 여부 조회")
    print("3. 포인트 조회")
    selectMenu = int(input(">"))
    if (selectMenu == 1):
        # 아이디와 비밀번호를 입력받는다.
        id_input = input("아이디를 입력해주세요: ")
        pw_input = input("비밀번호를 입력해주세요: ")
        check_res = idChecker(id_input, pw_input)
        if (check_res == 0):
            print("ID가 존재하지 않습니다.")
        elif (check_res == 1):
            print("패스워드가 잘못입력되었습니다.")
        else:
            print(id_input + "님, 환영합니다.")
            login[id_input] = True
    elif (selectMenu == 2):
        # 사용자 로그인 정보확인
        id_input = input("아이디를 입력해주세요: ")
        loginChecker(id_input)

