import pickle
def write():
    f=open("student.dat","wb")
    record=[]
    while True:
        rno=int(input("enter roll number"))
        name=input("enter name")
        marks=int(input("enter marks"))
        data=[rno,name,marks]
        record.append(data)
        ch=input("do you want to enter more records(y/n)")
        if ch in 'nN':
            break
    pickle.dump(record,f)
    print("record added successfully")
    f.close()

def read():
    f=open("student.dat","rb")
    print("contents are")
    s=pickle.load(f)
    try:
        while True:
            for i in s:
                print(i)
    except EOFError:
        print()
        f.close()
        

def search():
    f=open("student.dat","rb")
    found=0
    r=int(input("enter roll number of record to be searched"))
    s=pickle.load(f)
    try:
        for i in s:
            if i[0]==r:
                print("record of the entered roll number is",i)
                found=1
    except EOFError:
        f.close()

while True:
    print("1--to add a record")
    print("2--to display the records")
    print("3--to search a record")
    print("4--exit")
    ch=int(input("enter your choice"))
    if ch==1:
        write()
    elif ch==2:
        read()
    elif ch==3:
        search()
    elif ch==4:
        break
    else:
        print("INVALID CHOICE")