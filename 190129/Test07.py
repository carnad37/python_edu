def loginSystem(userDic):
    # for i in range(0,5,1): #로 반복횟수에 제한을 둘수있다.
    while True:
        #idChecker만 불러옴로 id만 체크
        id_input = idChecker(userDic)
        pw_input = input("비밀번호를 입력해주세요: ")
        if(pw_input == userDic[id_input]):
            break
        else:
            #userDIc에 없다면
            print("패스워드가 잘못입력되었습니다." + "\n")
    print(id_input + "님, 환영합니다.")
    #해당 아이디를 로그인상태(True)로 바꾸기위해 리턴받는다.
    return id_input

#login딕셔너리의 키값 체크
def idChecker(userDic):
    while True:
        id_input = input("아이디를 입력해주세요: ")
        check = id_input in userDic
        if (check):
            break
        print("존재하지 않는 아이디입니다." + "\n")
        #내부에서 체크한 id를 외부에서도 사용하기위해서 리턴.
    return id_input

# id, password 데이터
user = {"apple": "orange", "chair": "desk", "mouse": "keyboard", "person": "pocket"}
point = {"apple": 10000, "chair": 2000, "mouse": 700, "person": 70}

#login 딕셔너리 만들기, 기본값 False
user_id_List = list(user.keys())
login = {}
for i in range(0, len(user_id_List), 1):
    login[user_id_List[i]] = False

while True:
    # 메뉴제작
    print("1. 로그인")
    print("2. 사용자 로그인 여부 조회")
    print("3. 포인트 조회")
    selectMenu = int(input(">"))
    if (selectMenu == 1):
        #user딕셔너리만 넣어준다.
        #로그인 시스템내부에서 id입력체크 pw체크가 모두 이루워진다.
        id_input = loginSystem(user)
        #
        login[id_input] = True
    elif (selectMenu == 2):
        # 사용자 로그인 정보확인
        id_input = idChecker(login)
        if (login[id_input]):
            print(id_input + "님은 로그인 중입니다.")
        else:
            print(id_input + "님은 로그아웃 상태입니다.")
    elif (selectMenu == 3):
        # loginChecker로 login딕셔너리에 id존재를 확인
        id_input = idChecker(login)
        # 로그인 상태인지 아닌지를 확인
        if (login[id_input] == True):
            res_point = point[id_input]
            print(id_input + "님이 소유하신 포인트는", res_point, "입니다")
        else:
            print(id_input + "님은 로그아웃 상태입니다.")
            print("먼저 로그인을 해주십시오")
            id_input = loginSystem(user)
            login[id_input] = True
    else:
        print("잘못된 입력입니다.")

    print("\n" + "=" * 30 + "\n")