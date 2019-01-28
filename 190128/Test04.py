hlist={}
hlist['name'] = input("이름을 입력해주세요: ")
hlist['birth'] = input("생년월일을 입력해주세요: ")
hlist['age'] = input("나이를 입력해주세요: ")
print(hlist)
#for i in (0,3,1):



birthDay = hlist.get('birth')
birthMonth = birthDay[:2]
print(birthMonth)

checkEmail = 'email' in hlist
print(checkEmail)