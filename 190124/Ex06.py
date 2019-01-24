#입력값이 몇개인지 모르는 경우
#매개변수앞에 별을 붙여준다.

def add_many(*args):

    # for i in args:
    #     result = result + i
    return args
#
# result = add_many(1,2,3)
# print(result)
#
# result = add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)


aList =[]
aList = add_many(1,2,3,4,5)
checker = type(aList)
print(checker)
