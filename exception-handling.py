# try:
#     n1=int(input("Enter the num: "))
#     n2=int(input("Enter the num: "))
#     r=n1/n2
# except ValueError:
#     print("Zero Division Error")
# else:
#     print("result",r)
# finally:
#     print("Program executed successfully")

# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
# while True:
#     import math
#
#     try:
#         n=int(input("Enter the number: "))
#         print(math.factorial(n))
#         break
#     except ValueError:
#         print("Value Error")
# import math
# def fact():
#     try:
#         n=int(input("Enter the number: "))
#         print(math.factorial(n))
#     except ValueError:
#         print("Value Error")
#         fact() #recursion
# fact()

# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# while True:
#     try:
#         print("1.Addition")
#         print("2.substraction")
#         print("3.multiplication")
#         print("4.division")
#         print("5.exit")
#
#         ch = int(input("Enter the choice: "))
#         if ch in [1,2,3,4]:
#             n1=int(input("Enter num 1: "))
#             n2=int(input("Enter num 2: "))
#             a=n1+n2
#             s=n1-n2
#             m=n1*n2
#             d=n1/n2
#     except ZeroDivisionError:
#         print('Zero division error')
#     except ValueError:
#         print("Value Error")
#     else:
#         if ch==1:
#             print("add",a)
#         elif ch==2:
#             print('sub',s)
#         elif ch==3:
#             print("multiply",m)
#         elif ch==4:
#             print("div",d)
#         else:
#             exit()
# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
# try:
#     n=input("file name: ")
#     f=open(n,'r')
#     s=f.read()
# except:
#     print("file does not exist")
# else:
#     print(s)

#Given a Dictionary
#
# d={"name":"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist
# try:
#     key=input("Enter the key: ")
#     print(d[key])
# except KeyError:
#     print("Key does not exist")

# as keyword
# try:
#     n1=int(input("Enter the num: "))
#     n2=int(input("Enter the num: "))
#     r=n1/n2
# except Exception as e :
#     print(e)
#     print(type(e))
# else:
#     print("result",r)
# finally:
#     print("Program executed successfully")
# class MyException(Exception):
#     pass
# # raise
# try:
#     n=int(input("Enter the age: "))
#     if (n<18):
#        raise MyException("Not eligible for voting")
#     else:
#         print("Eligible for voting")
# except MyException as e:
#     print(e)
#
# # raise our own exception
# class MyException(Exception):
#     pass

#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"
# try:
#     n=int(input("Enter the number: "))
#     if n<=0:
#         raise ValueError("Number must be positive")
# except ValueError as e:
#     print(e)


#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")
# class InvalidPasswordError(Exception):
#     pass
# try:
#     paswrd=input("Enter the password: ")
#     if len(paswrd)<8:
#         raise InvalidPasswordError("Password should be 8 character")
# except InvalidPasswordError as e:
#     print(e)
# else:
#     print("Password Entered successful")

#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")
# class InsuffientBalanceError(Exception):
#     pass
# try:
#     n=int(input("Enter the amount: "))
#     balance=10000
#     if n>balance:
#         raise InsuffientBalanceError("Not Enough Balance.Transaction Failed")
# except InsufficientBalanceError as e:
#     print(e) 
