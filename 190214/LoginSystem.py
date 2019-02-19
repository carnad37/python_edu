import time

file_patH = "D:\\hhs2\\file\\userdata.txt"
"""
저장할 파일 형식
저장은 String으로 라인마다 입력.
아이디,비밀번호,이름,이메일,로그인시간
구분은 " "나 ","로 가능. 안전성을 위해 ","로 하자.
또한 입력금지 단어의 설정 필요.(나중에)

클래스에서 객체로 생성해, list에 추가.
"""

# class userData:
#     def __init__(self,id,pw,name,email):
#         self.id = id
#         self.pw = pw
#         self.name = name
#         self.email = email
#
#
#     def loginSystem(self,id,pw):
#         self.id
def lastLoginTime(self):
    now = time.localtime()
    self.lastlogin = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

#signSystem을 통해 userData의 객체를 생성해 리스트에 추가한다.
def signSystem():
    signSystemCheker = True
    while(signSystemCheker):
        print("회원가입을 시작합니다.")
        id = input("아이디를 입력해주세요: ")
        pw = pwCheck()
        name = input("이름을 입력해주세요: ")
        email = input("이메일을 입력해주세요: ")

#saveUserData에서 취소를 했을시 signSystem 반복.


def pwCheck():
    pwChecker = True
    while(pwChecker):
        pw = input("패스워드를 입력해주세요: ")
        for i in range(0, 5, 1):
            pwCheck = input("패스워드를 확인해주세요: ")
            if pw != pwCheck:
                rNum = 5-i
                print("잘못된 입력입니다.")
                print("남은 횟수 :", rNum)
            else:
                pwChecker = False
                break
            if i == 5:
                print("패스워드를 처음부터 다시 입력해주세요.")

def saveUserData(id,pw,name,email):
    print("ID :",id)
    print("이름 :",name)
    print("E-mail :",email)
    print("이대로 진행하시겠습니까?")
    print("진행하실시 1, 취소하시고 다시 입력하시려면 2를 입력해주세요.")
    while(True):
        saveChecker = input(">")
        if saveChecker==1:
            saveData = userData(

        else:
            break





