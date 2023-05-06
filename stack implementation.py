def isempty(stack):
    if stack==[]:
        return True
    else:
        return False
    
def push(stack,item):
    stack.append(item)
    top=len(stack)-1

def pop(stack):
    if isempty(stack):
        return "UNDERFLOW"
    else:
        item=stack.pop()
        if len(stack)==0:
            top=None
        else:
            top=len(stack)-1
        return item

def peek(stack):
    if isempty(stack):
        return "UNDERFLOW"
    else:
        top=len(stack)-1
        return(stack[top])
    
def display(stack):
    if isempty(stack):
        print("UNDERFLOW")
    else:
        top=len(stack)-1
        print(stack[top])
        for a in range(top-1,-1,-1):
            print(stack[a],end=" ")
#execution
st=[]
top=None
while True:
    print("1--to add an element")
    print("2--to delete an element")
    print("3--to display the topmost element")
    print("4--to display the status of stack")
    print("5--exit")
    ch=int(input("enter your choice"))
    if ch==1:
        item=int(input("enter an element"))
        push(st,item)
    elif ch==2:
        item=pop(st)
        if item=="UNDERFLOW":
            print("stack empty")
        else:
            print("the deleted element is",item)
    elif ch==3:
        item=peek(st)
        if item=="UNDERFLOW":
            print("stack empty")
        else:
            print("the topmost element is",item)
    elif ch==4:
        display(st)
    elif ch==5:
        break
    else:
        print("INVALID CHOICE")
    