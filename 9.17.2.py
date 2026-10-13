#学生系统管理     #方法方
class Student:
    def __init__(self,filename):
        self.filename = filename
        self.id={}
        self.grades = {}
        # self.part=[]换成局部变量可以有效避免后面名字重复越叠越多的问题

    def load(self):
        with open(self.filename,"r",encoding="utf-8")as f:
            for line in f:
                line = line.strip()
                parts = line.split(",")
                if len(parts)<3:
                    print("出现格式错误")
                    continue
                name = parts[0]
                student_id = parts[1]
                try:
                    score = int(parts[2])
                except ValueError:
                    print(f"跳过分数的不是数字的行：{line}")
                    continue
                self.id[name]=student_id
                self.grades[student_id]=score

    def display(self):
        # part = []
        # for name in self.id:
        #     part.append(name)
        # return part
        return list(self.id.keys())#一句概括上面代码
    def find_grade(self,student_id):
            if student_id in self.grades.keys():
                return self.grades[student_id]
            # return self.grades.values()返回字典加上所有的人名
            return "查无此学号"
    def average(self):
        return sum(self.grades.values())/len(self.grades)

    def highest(self):
        return max(self.grades.values())

    def add(self,name,student_id,score):
            # a = input("请输入要添加的姓名：")
            # b = input("请输入要添加的学生的学号：")
            # c = int(input("请输入添加的学生的成绩："))
            # self.id[a]=b
            # self.grades[b]=int(c)
            if name in self.id:
                print("学生姓名已经存在")
                return False
            if student_id in self.grades:#in 查字典时只查 key，不查 value
                print("学生学号已经存在")
                return False
            self.id[name]=student_id
            self.grades[student_id]=score#两表必须同时，否则就会混乱
            return True#方法返回 True/False 把成功/失败告诉调用方，提示语归调用方管
    
    def remove(self,name):
        if name not in self.id:
            print("您要删除的学生不存在")
            return
        sid = self.id.pop(name)
        self.grades.pop(sid,None)
        print("删除成功")

    def update(self,student_id,score):
        self.grades[student_id]=score


    def print_info(self,name,student_id):
        print(f"学生系统所有姓名：{self.display(name)}")
        print(f"学生姓名：{name},学生成绩：{self.find_grade(student_id)}")
        print(f"平均分为：{self.average()}")
        print(f"最高分是{self.highest()}")

    def save(self,outfile):
        with open(outfile,"w",encoding = "utf-8")as f:
            for name,student_id in self.id.items():
                score = self.grades[student_id] 
                f.write(f"{name},{student_id},{score}\n")
my = Student("student.txt")
my.load()
# my.print_info("张三","2024001")
# my.print_info("王五","2024003")
# my.add("小龙","2024008",99)
# my.remove("王五","2024003")
# my.update("2024001",100)
# my.save("student_out.txt")


#调用方
while True:
    print("\n========= 学生管理系统 =========")
    print("1. 查看平均分")
    print("2. 查看最高分")
    print("3. 查看某学生成绩")
    print("4. 添加学生")
    print("5. 删除学生")
    print("6. 保存到文件")
    print("7.查看全部学生姓名及人数")
    print("8. 退出")
    choice = input("请输入选择（1-8）：")
    if choice == "1":
        print(f"平均分是：{my.average():.1f}")
    elif choice == "2":
        print(f"最高分是：{my.highest()}")
    elif choice == "3":
        a = input("请输入要查询学生的学号：")
        print(f"该学生的成绩为：{my.find_grade(a)}")
    elif choice == "4":      
        name_new = input("请输入要添加的学生姓名：")
        id_new = input("请输入要添加的学生的学号：")
        try:
            score_new = int(input("请输入学生的成绩："))
            if my.add(name_new,id_new,score_new):
                print("添加完成")#删除少输入，添加多查重复
            else:
                print("请重新输入!")
                break
        except ValueError:
            print("输入的不是数字,请重新输入")
        
    elif choice == "5":
        x = input("请输入要删除的学生姓名：")
        my.remove(x)
    elif choice == "6":
        my.save("student_out.txt")
        print("保存完成")
    elif choice == "7":
        result=my.display()
        print(result)
        print(len(result))
    elif choice == "8":
        print("再见！")
        break
    else:
        print("输入无效，请重新输入")
       # self.id 本来就是"姓名 → 学号"的字典，学号可以反查出来。
