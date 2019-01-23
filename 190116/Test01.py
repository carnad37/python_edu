id_List = ["chailin", "carnad", "riaiya", "naity", "magical"]

input_id = input("아이디를 입력해주세요: ")
"""
id_search = id_List.count(input_id)
if id_search > 0:
    print("환영합니다.")
else:
    print("아이디를 찾을 수 없습니다.")
"""
def toString(a):
    addString = " "
    result = addString.join(a)
    return result

id_ListString = toString(id_List)

id_search = id_ListString.find(input_id)
if id_search == -1:
    print("아이디를 찾을 수 없습니다.")
else:
    print("환영합니다.")
