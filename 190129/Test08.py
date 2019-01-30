#입력받은 값들로, 각각의 리스트에서 id와 pw를 체크한다.
#체크한 결과는 check_res를 리턴하여 로그인시스템에서 판별한다.
def idChecker(id_List,pw_List,id,pw):
    check_res = 0
    for i in range(0,len(id_List),1):
        if(id == id_List[i]):
            check_res = 1
            break
    if(check_res == 1):
        for i in range(0,len(pw_List),1):
            if(pw == pw_List[i]):
                check_res = 2
                break

    return check_res

#전체적인 로그인 시스템
#기본적으로 로그인이 될때까지 반복된다.
#로그인시스템내에서 idChecker를 호출
def loginSystem(id_List, pw_List):
    # 아이디와 비밀번호를 입력받는다.
    #for i in range(0,5,1): #로 반복횟수에 제한을 둘수있다.
    while True:
        id_input = input("아이디를 입력해주세요: ")
        pw_input = input("비밀번호를 입력해주세요: ")
        #리스트, 입력받은 아이디와 비밀번호를 매개변수로 넣어줌.
        check_res = idChecker(id_List, pw_List, id_input, pw_input)
        # id와 pw를 체크하는 함수
        # check_res가 0일시 id가 없다.
        # check_res가 1일시 id는 있는데 비밀번호가 없다.
        # check_res가 2일시 로그인가능.
        if (check_res == 0):
            print("ID가 존재하지 않습니다."+"\n")
        elif (check_res == 1):
            print("패스워드가 잘못입력되었습니다."+"\n")
        else:
            print(id_input + "님, 환영합니다.")
            return id_input


def loginChecker(login):
    while True:
        id_input = input("아이디를 입력해주세요: ")
        check = id_input in login
        if(check):
            break
        print("존재하지 않는 아이디입니다."+"\n")
    return id_input


#1~3까지의 숫자만 입력가능.

#id, password 데이터
user = {"apple":"orange","chair":"desk","mouse":"keyboard","person":"pocket"}
user_id_List = list(user.keys())
user_pw_List = list(user.values())
login = {}
for i in range(0,len(user_id_List),1):
    login[user_id_List[i]]=False
point = {"apple":10000,"chair":2000,"mouse":700,"person":70}

while True:
    # 메뉴제작
    print("1. 로그인")
    print("2. 사용자 로그인 여부 조회")
    print("3. 포인트 조회")
    selectMenu = int(input(">"))
    if (selectMenu == 1):
        #유저 id, pw리스트를 매개변수로 받아서 로그인 시스템에 넣어줌.
        #id와 pw는 시스템 내부에서 루프를 통해 입력받음.
        #입력받고 난뒤 바로 login 딕셔너리에 값을 넣어줄수 없으므로(전역변수에 손을대야함)
        #id를 리턴받고 후에 아이디에 True값을 넣어준다.
        login_id = loginSystem(user_id_List,user_pw_List)
        login[login_id] = True
    elif (selectMenu == 2):
        # 사용자 로그인 정보확인
        id_input =loginChecker(login)
        if(login[id_input]):
            print(id_input+"님은 로그인 중입니다.")
        else:
            print(id_input+"님은 로그아웃 상태입니다.")
    elif(selectMenu == 3):
        #loginChecker로 login딕셔너리에 id존재를 확인
        id_input = loginChecker(login)
        #로그인 상태인지 아닌지를 확인
        if(login[id_input]==True):
            res_point = point[id_input]
            print(id_input+"님이 소유하신 포인트는",res_point,"입니다")
        else:
            print(id_input+"님은 로그아웃 상태입니다.")
            print("먼저 로그인을 해주십시오")
            login_id = loginSystem(user_id_List, user_pw_List)
            login[login_id] = True
    else:
        print("잘못된 입력입니다.")

    print("\n"+"="*30+"\n")