def peopleInfo(path_file):
    #데이터를 리스트로 만들어주는 함수
    readfile = open(path_file,'r')
    checkList = []
    saveList = []
    for line in readfile:
        line = line.strip()
        checkList = line.split()
        checkList[1] = int(checkList[1])
        saveList.append(checkList)
    #여기서
    readfile.close()
    return saveList

def nameSearch(name,dList):
    pickList = []
    for i in range(0,len(dList),1):
        if dList[i][0]==name:
            pickList = dList[i]
            break
    return pickList

def jobSearch(job,dList):
    pickList = []
    for i in range(0,len(dList),1):
        if dList[i][2]==job:
            pickList = dList[i]
            break
    return pickList

def namefirstString_AgeSum(name,dList):
    sum = 0
    for i in range(0,len(dList),1):
        if dList[i][0][0] == name:
            sum += dList[i][1]
    return sum

def twentyPeopleNamePrint(age,dList):
    sum = 0
    print("나이가 %d대인 사람들의 이름은"%age,end="")
    for i in range(0,len(dList),1):
        peopleAge = dList[i][1]
        if (peopleAge>=age)&(peopleAge<(age+10)):
            name = dList[i][0]
            print(" ("+name+")",end="")
    print("이다.")

def jobLastTwoString_Name(job,dList):
    nameList=[]
    for i in range(0,len(dList),1):
        if dList[i][2][-2:] == job:
            nameList.append(dList[i][0])
    return nameList


info_path = "D:\\hhs2\\file\\peopleInfo.txt"
peopleData = peopleInfo(info_path)
print(peopleData)
#tom의 나이
tomList = nameSearch("tom",peopleData)
tomAge = tomList[1]
print("tom의 나이는",tomAge,"세")

#직업이 간호사인 사람의 나이
nurseList = jobSearch("nurse",peopleData)
nurseAge = nurseList[1]
print("간호사의 나이는",nurseAge,"세")

#이름이 b로 시작하는 사람들의 나이의 합

bFirstStringAgeSum = namefirstString_AgeSum("b",peopleData)
print("이름이 B로 시작하는 사람들의 나이의 합은",bFirstStringAgeSum,"세이다.")

#나이가 20대인 사람들의 이름

twentyPeopleNamePrint(20,peopleData)

#직업의 마지막 두자가 or 인 사람의 이름

nameList = jobLastTwoString_Name("or",peopleData)
print(nameList)