#write operation
# f=open('k.txt','w')
# f.write(string)
# f.write("hello\n")
# f.write("python\n")
# f.writelines(list)
# f.writelines(['hello\n','python\n'])
# f.close

# f=open('k.txt','r')
# s=f.read()
# print(s)
# f=open('k.txt','r')
# r=f.readlines()
# print(r)


# # #write a program to read a text file and displays the number of lines in a file
# f=open('k.txt','r')
# s=f.readlines()
# print(len(s))
# f.close()
# # #write a program to display the number of words in a file
# f=open('k.txt','r')
# s=f.read()
# print(len(s.split()))
# f.close()
# # #write a program to update the second line in a file
# f=open('k.txt','r')
# s=f.readlines()
# s[1]="new line\n"
# f.close()
#
# f=open('k.txt','w')
# f.writelines(s)
# f.close()
# # #write a program to display the last 5 lines in a file
# f=open('k.txt','r')
# s=f.readlines()
# print(s[-5:])
# f.close()
# # #program to search a particular word in a file
# f=open('k.txt','r')
# n=input("Enter the word: ")
# s=f.read()
# if n in s:
#     print('found')
# else:
#     print('not found')
# f.close()
# #find the number of letters,digits,and spaces in a file
# f=open('k.txt','r')
# s=f.read()
# digit=0
# letters=0
# space=0
# for i in s:
#     if i.isalpha():
#         letters=letters+1
#     elif i.isdigit():
#         digit = digit + 1
#     elif i.isspace():
#         space=space+1
# else:
#     print("invalid")
# print(letters)
# print(digit)
# print(space)
# f.close()
#reverse the lines in a file
# f=open('k.txt','r')
# s=f.readlines()
# n=s[::-1]
# f.close()
# f=open('k.txt','w')
# f.writelines(n)
# f.close()

# append
# f=open('k.txt','a')
# f.write("python\n")
# f.close()

# write a program to append the content from one file into another text file
# f=open('k.txt','r')
# g=open('new.txt','a')
# s=f.read()
# g.write(s)
# f.close()
# g.close()

# f=open('k.txt','a+')
# f.write('python')
# f.seek(0)
# s=f.read()
# print(s)

# import os
# os.remove('k.txt')

