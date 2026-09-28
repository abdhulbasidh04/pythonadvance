# 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
#
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.
#
# class Circle:
#     def __init__(self):
#         self.radius=int(input("Enter the radius: "))
#     def getarea(self):
#         area=3.14*self.radius**2
#         print(area)
#     def getperimeter(self):
#         perimeter=2*3.14*self.radius
#         print(perimeter)
# r=Circle()
# r.getarea()
# r.getperimeter()

# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance
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