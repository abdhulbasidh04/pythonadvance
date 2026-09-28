# class Person:
#     def __init__(self): #construct method
#                         #used to initialize object
#         self.name=input("Enter name: ")
#         self.age=int(input("Enter age: "))
#     def show(self):
#         print(self.name,self.age)
# p1=person()
# p1.show()
# p2=person()
# p2.show()

# define a class named employee with attributes employee id name,age,salary,designation and methods getsalary() and and showpersonaldetails()
# class Employee:
#     def __init__(self):
#         self.empid=int(input("Enter the empid: "))
#         self.name=input("Enter the name: ")
#         self.age=int(input("Enter the age: "))
#         self.salary=int(input("Enter the salary: "))
#         self.designation=input("Enter the designation: ")
#     def getsalary(self):
#         print(self.salary)
#
#     def show(self):
#         print(self.name,self.age)
# e1=Employee()
# e1.getsalary()
# e1.show()

# define a class named student with attribute rollno,name,mark of 3 sub and method display() to display roll number and total mark of that stusent create a student object and call the method
# class Student:
#     def __init__(self):
#         self.rollno=int(input("Enter the rollno: "))
#         self.name=input("Enter the name: ")
#         self.mark1=int(input("Enter the mark1: "))
#         self.mark2 = int(input("Enter the mark2: "))
#         self.mark3 = int(input("Enter the mark3: "))
#     def display(self):
#         print("rollno:",self.rollno)
#         print("Total marks",self.mark1+self.mark2+self.mark3)
# s=Student()
# s.display()

# create a class named book with attributes title,author,price,pages,language and methods
# gettitle(),getauthor(),getprice()
# settitle(),setauthor(),setprice()
#create a book object and call  the method
# class Book:
#     def __init__(self):
#         self.title=input("Enter the title: ")
#         self.author=input("Enter the author: ")
#         self.price=int(input("Enter the price: "))
#         self.pages=int(input("Enter the pages: "))
#         self.language=input("Enter the language: ")
#     def gettitle(self):
#         print(self.title)
#     def getauthor(self):
#         print(self.author)
#     def getprice(self):
#         print(self.price)
#     def settitle(self):
#         self.title=input("Enter the new title: ")
#         self.gettitle()
#     def setauthor(self):
#         self.author=input("Enter the new author: ")
#     def setprice(self):
#         self.price=int(input("Enter the new price: "))
# b=Book()
# b.gettitle()
# b.getauthor()
# b.getprice()
# b.settitle()
# b.setauthor()
# b.setprice()

# create a class named account with attributes accntname,accntnumber,balance
# methods are withdraw(),deposite(),showbalance()
# class Account:
#     def __init__(self):
#         self.accntname=input("Enter account holder name: ")
#         self.accntno=int(input("Enter the account no: "))
#         self.balance=int(input("Enter the accnt balance: "))
#     def withdraw(self):
#         amount=int(input("Enter the amount to withdraw: "))
#         if(amount>self.balance):
#             print("insufficient balance")
#         self.balance-=amount
#         self.showbalance()
#     def deposit(self):
#         amount=int(input("Enter the amount to deposit: "))
#         self.balance+=amount
#         self.showbalance()
#     def showbalance(self):
#         print("current balance",self.balance)
# a1=Account()
# # a.withdraw()
# # a.deposit()
# # a.showbalance()
# a2=Account()
# l=[a1,a2]
# for i in l:
#     print(i.accntname,i.accntno)
#     i.showbalance()


# Banking operation menu driven using (class and list)

# class Account:
#     def __init__(self):
#         self.accntno=int(input("Enter the account no: "))
#         self.accntname=input("Enter the name: ")
#         self.balance=int(input("Enter the balance: "))
#     def withdraw(self):
#         amount=int(input("Enter the amount to withdraw: "))
#         if(amount>self.balance):
#             print("insufficient balance")
#         self.balance-=amount
#         self.showbalance()
#     def deposit(self):
#         amount=int(input("Enter the amount to deposit: "))
#         self.balance+=amount
#         self.showbalance()
#     def showbalance(self):
#         print("current balance",self.balance)
# l=[]
# while(1):
#     print("1.create a new account")
#     print("2.withdraw")
#     print("3.deposit")
#     print("4.show balance")
#     print("5.Exit")
#     ch=int(input("Enter the choice: "))
#     if ch==1:
#         a=Account()
#         l.append(a)
#         print(l)
#     elif ch==2:
#         n=int(input("Enter the account number: "))
#         for i in l:
#             if i.accntno==n:
#                 i.withdraw()
#                 break
#         else:
#             print("Account does not exist")
#     elif ch==3:
#         n=int(input("Enter the account number: "))
#         for i in l:
#             if i.accntno==n:
#                 i.deposit()
#                 break
#         else:
#             print("Account does not exist")
#     elif ch==4:
#         n=int(input("Enter the account number: "))
#         for i in l:
#             if i.accntno==n:
#                 i.showbalance()
#                 break
#         else:
#             print("Account does not exist")
#     elif ch==5:
#         exit()

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


