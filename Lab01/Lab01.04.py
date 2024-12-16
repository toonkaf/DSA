"""Student Class"""
def stc():
    """stc"""
    lst = []
    for i in range(15):
        lst.append(input())
    x = input()
    if x in lst:
        if lst[lst.index(x)-2] == "Male":
            if int(lst[lst.index(x)-1]) < 15:
                print("Master",end=" ")
            else: 
                print("Mr",end = " ")
        else:
            print("Miss",end = " ")
        print(lst[lst.index(x)-3],end=" ")
        print("(",lst[lst.index(x)-1],")",end=" ",sep="")
        print("ID:",x,end = " ")
        gpa = round(float(lst[lst.index(x)+1]),2)
        if str(gpa)[-3] != ".":
            gpa = str(gpa) + "0"
        print("GPA",gpa)
    else:
        print("Student not found")
stc()
