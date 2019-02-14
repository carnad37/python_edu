class StudentScoreData:
    def __init__(self, file_path):
        readfile = open(file_path,'r')
        self.avg_List = []
        self.name_List = []
        count = 0
        check_List = []
        for line in readfile:
            line = line.rstrip("\n")
            check_List = line.split(",")
            sum_num = 0
            avg_num = 0
            if count>0:
                # for i in check_List[1:]:
                #     i=int(i)
                #     sum_num += i
                sum_num = sum(list(map(int,check_List[1:])))
                avg_num = sum_num / (len(check_List) - 1)
                self.avg_List.append(avg_num)
                self.name_List.append(check_List[0])
            count += 1
        readfile.close()

    def score_sort_student(self):
        sort_List = sorted(self.avg_List)
        self.max_avg = sort_List[len(self.avg_List)-1]
        self.min_avg = sort_List[0]
        search = self.avg_List.index(self.max_avg)
        self.max_name = self.name_List[search]
        search = self.avg_List.index(self.min_avg)
        self.min_name = self.name_List[search]

    def print_avg_scroe(self):
        # 모든 학생의 평균점수를 호출
        for i in range(0, len(self.avg_List), 1):
            name = self.name_List[i]
            avg = self.avg_List[i]
            print("%s의 평균점수는 %d이다" % (name, avg))

ssd = StudentScoreData("d:\\hhs2\\file\\subjectScore.csv")
ssd.print_avg_scroe()
ssd.score_sort_student()
listd =[]
listd.append(ssd)
print(listd)
print(ssd.avg_List)
print("")
print("가장 점수가 높은 학생의 이름은 %s이다."%ssd.max_name)
print("가장 점수가 낮은 학생의 점수는 %d이다."%ssd.min_avg)