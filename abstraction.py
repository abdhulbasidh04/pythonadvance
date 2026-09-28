# # from abc import ABC,abstractmethod
# # class Shape(ABC):
# #     @abstractmethod
# #     def area(self):
# #         pass
# #     def perimeter(self):
# #         pass
# # class Rectangle(Shape):
# #     def __init__(self):
# #         self.length=int(input("Enter the length: "))
# #         self.breadth=int(input("Enter the breadth: "))
# #     def area(self):
# #         print("area:",self.length*self.breadth)
# #     def perimeter(self):
# #         print("perimeter:",2*(self.length+self.breadth))
# # class Square(Shape):
# #     def __init__(self):
# #         self.side=int(input("Enter the no of sides: "))
# #     def area(self):
# #         print("area of square:",self.side*self.side)
# #     def perimeter(self):
# #         print("perimeter of square:",4*self.side)
# #
# # r=Rectangle()
# # r.area()
# # r.perimeter()
# #
# # s=Square()
# # s.area()
# # s.perimeter()
#
#
# # create an abstract class Employee with an abstract method calculate salary()
# from abc import ABC,abstractmethod
# class Employee(ABC):
#     def __init__(self):
#         self.name=input("Enter the name: ")
#         self.id=int(input("Enter the id: "))
#         self.age=int(input("Enter the employee age: "))
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
# class FullTimeEmployee(Employee):
#     def __init__(self):
#         super().__init__()
#         self.salary=int(input("Enter the salary: "))
#     def calculate_salary(self):
#         print("Monthly salary is:",self.salary)
# class PartTimeEmployee(Employee):
#     def __init__(self):
#         super().__init__()
#         self.hours=int(input("Enter the working hours: "))
#         self.rate=int(input("Enter the rate per hours: "))
#     def calculate_salary(self):
#         print("salary:",self.hours*self.rate)
# f=FullTimeEmployee()
# f.calculate_salary()
#
# p=PartTimeEmployee()
# p.calculate_salary()
