# A file totalstudents.txt contains the names of all students in a class,
# f=open('totalstudents.txt','w')
# s=f.writelines(['abhi\n','basi\n','arun\n','raju\n'])
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# f=open('passedstudents.txt','w')
# s=f.writelines(['basi\n','arun\n'])
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.
# f=open('totalstudents.txt','r')
# g=open('passedstudents.txt','r')
# s1=f.readlines()
# s2=g.readlines()
# h=open('failed.txt','w')
# for i in s1:
#     if i not in s2:
#         h.write(i)
# f.close()
# g.close()
# h.close()