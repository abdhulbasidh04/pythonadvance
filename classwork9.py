# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1.Add Student(roll no,name,marks)
# 2.Update Marks
# 3.Display All Student Details
# 4.Search Student by Roll Number
# 5.Delete Student
# 6.Exit
# Store student records in a list and perform all operations using the student's roll number.
class Student:
    def __init__(self):
        self.rollno=int(input("Enter the rollno: "))
        self.name=input("Enter the name: ")
        self.marks=int(input("Enter the marks: "))
    def update_marks(self):
        self.marks=int(input("Enter the new marks: "))
    def display(self):
        print("roll no",self.rollno)
        print("Name",self.name)
        print("Mark",self.marks)
l=[]
while(1):
    print("1.Add Student Details")
    print("2.Update Marks")
    print("3.Display All Student Details")
    print("4.Search Student by Roll Number")
    print("5.Delete Student")
    print("6.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        s=Student()
        l.append(s)
        print(l)
    elif ch==2:
        n=int(input("Enter the rollno: "))
        for i in l:
            if i.rollno==n:
                i.update_marks()
                break
        else:
            print("invalid rollno")
    elif ch==3:
        for i in l:
            i.display()
    elif ch==4:
        n=int(input("Enter the rollno: "))
        for i in l:
            if i.rollno==n:
                i.display()
                break
        else:
            print("Invalid rollno")
    elif ch==5:
        n = int(input("Enter the rollno: "))
        for i in l:
            if i.rollno == n:
                l.remove(i)
                break
        else:
            print("invalid rollno")
    elif ch==6:
        exit()