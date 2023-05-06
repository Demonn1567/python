def create():
    f=open("sample.txt","w")
    f.write("what is your name\n")
    f.write("my name is\n")
    print("file created successfully")
    f.close()

def count():
    f=open("sample.txt","r")
    count=0
    line=f.read()
    for i in line:
        if i in "aeiouAEIOU":
            count=count+1
    print("the number of vowels are",count)
    f.close()

def wordcount():
    f=open("sample.txt","r")
    f.seek(0)
    line=f.read()
    word=line.split()
    n=len(word)
    print("the number of words are",n)
    f.close()

#main
while True:
    print("1--to create a text file")
    print("2--to count the number of vowels")
    print("3--to count the number of words")
    print("4--exit")
    ch=int(input("enter your choice"))
    if ch==1:
        create()
    elif ch==2:
        count()
    elif ch==3:
        wordcount()
    elif ch==4:
        break
    else:
        print("INVALID CHOICE")
