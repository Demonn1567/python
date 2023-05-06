import csv
def write():
    f=open("employee.csv","w",newline="\n")
    n=int(input("enter number of records to be added"))
    stuwritter=csv.writer(f)
    stuwritter.writerow(['eid','ename','esal'])
    for i in range(n):
        eid=int(input("enter employee id"))
        ename=input("enter employee name")
        esal=int(input("enter employee salary"))
        sturec=[eid,ename,esal]
        stuwritter.writerow(sturec)
    print("record added successfully")
    f.close()

def read():
    f=open("employee.csv","r",newline="\n")
    stufr=csv.reader(f)
    print("contents are")
    for rec in stufr:
        print(rec)
    f.close()

def search():
    f=open("employee.csv","r",newline="\n")
    r=int(input("enter employee id to be searched"))
    stufr=csv.reader(f)
    for rec in stufr:
        if rec[0]==r:
            print("record of the entered roll number is",r)
    f.close()

def count():
    f=open("employee.csv","r",newline="\n")
    count=0
    next(f)
    stufr=csv.reader(f)
    for rec in stufr:
        count=count+1
    print("the number of records are",count)
    f.close()

#main
while True:
    print("1--to add a record")
    print("2--to read the records")
    print("3--to search a record")
    print("4--to count the number of records")
    print("5--exit")
    ch=int(input("enter your choice"))
    if ch==1:
        write()
    elif ch==2:
        read()
    elif ch==3:
        search()
    elif ch==4:
        count()
    elif ch==5:
        break
    else:
        print("INVALID CHOICE")