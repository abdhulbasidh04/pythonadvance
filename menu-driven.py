# 1.file read
# 2.file write
# 3.file append
# 4.file search
# 5.file delete
# 6.exit
def file_read():
    try:
        filename=input("Enter file name: ")
        f=open(filename,'r')
        s=f.read()
        print(s)
        f.close()
        return
    except:
        print("File does not exist")

def file_write():
    filename=input("Enter file name: ")
    f=open(filename,'w')
    f.write(input("Enter the content: "))
    f.close()
    return

def file_append():
    filename=input("Enter file name: ")
    f=open(filename,'a+')
    f.write(input("enter the word: "))
    f.seek(0)
    s=f.read()
    print(s)
    f.close()
    return

def file_search():
    try:
        filename=input("Enter file name: ")
        f=open(filename,'r')
        s=f.read()
        c=input("Enter the word: ")
        if c in s:
            print("the content is in the file")
        else:
            print("the content is not in the file")
        f.close()
        return
    except:
        print("File does not found")

def file_delete():
    filename=input("Enter file name: ")
    import os
    os.remove(filename)
    return

while(True):
    print('menu driven file operation')
    print('1.file read')
    print('2.file write')
    print('3.file append')
    print('4.file search')
    print('5.file delete')
    print('6.exit')
    ch=int(input("Enter your choice: "))
    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_delete()
    else:
        break

