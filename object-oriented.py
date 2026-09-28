# class Parent:
#     def m1(self):
#         print("in parent class method m1")
#     def m2(self):
#         print("in parent method m2")
#
# # p=Parent()
# # p.m1()
# # p.m2()
#
# class Child(Parent):
#     def m1(self):
#         super().m1()
#         print("in child class method m1") #method overriding
#     def m3(self):
#         print("in child class method m3")
# c=Child()
# c.m1()
# c.m2()
# c.m3()

# single-level-inheritance
# class Person:
#     def __init__(self):
#         self.name=input("Enter the name: ")
#         self.age=int(input("Enter the age: "))
#     def show(self):
#         print("Name",self.name,"Age",self.age)
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=input("Enter the rollno: ")
#         self.mark=int(input("Enter the mark: "))
#     def show(self):
#         super().show()
#         print("Rollno",self.rollno,"Mark",self.mark)
#     def update_mark(self):
#         self.mark=int(input("Enter the new mark: "))
# s=Student()
# s.show()
# s.update_mark()

# class Category:
#     def __init__(self):
#         self.category_name=input("Enter the catogery name: ")
#     def showcategory(self):
#         print(self.category_name)
#
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.product_name=input("Enter the product name: ")
#         self.price=int(input("Enter the price: "))
#         self.quantity=int(input("Enter the quantity: "))
#     def total_price(self):
#         print(total_pri=self.price*self.quantity)
# p=Product()
# p.total_price()

class Company:
    def __init__(self):
        self.company_name=input("Enter the company name: ")
        self.company_location=input("Enter the company location: ")
    def display(self):
        print(self.company_name,self.company_location)

class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empname=input("Enter the employee name: ")
        self.salary=int(input("Enter the salary: "))
    def display(self):
        super().display()
        print("Employee name:",self.empname,"Employye salary:",self.salary)
    def update_salary(self):
        self.salary=self.salary*0.10+self.salary
        print("updated salary is:",self.salary)
e=Employee()
e.display()
e.update_salary()
