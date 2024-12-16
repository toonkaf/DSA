"""Student Class with Class"""
class Student:
    def __init__(self,name,sex,age,id,gpa):
        self.name = name
        self.sex = sex
        self.age = age
        self.id = id
        self.gpa = gpa

    def reg(self):
        if self.sex == "Male":
            return f"Mr {self.name} ({self.age}) ID: {self.id} GPA {self.gpa:.2f}"
        else:
            return f"Miss {self.name} ({self.age}) ID: {self.id} GPA {self.gpa:.2f}"
    def ide(self):
        return self.id

def main():
    """main"""
    idandword = []
    for i in range(3):
        stu = Student(input(),input(),input(),input(),float(input()))
        idandword.append(stu.ide())
        idandword.append(stu.reg())
    x = input()
    if x in idandword:
        print(idandword[idandword.index(x) + 1])
    else:
        print("Student not found")
main()
