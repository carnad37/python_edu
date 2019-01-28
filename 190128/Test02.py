student = {'name' : '홍길동'}
student['department'] = '경영학과'
student['학번'] = '20191254'

sKeys = student.keys()
print(sKeys)

sKeys_list = list(sKeys)
print(sKeys_list)
print()
sValues = student.values()
print(sValues)

sValues_list = list(sValues)
print(sValues_list)
print()
sItem = student.items()
print(sItem)

sItem_list = list(sItem)
print(sItem_list)
print()

student.clear()
print(student)