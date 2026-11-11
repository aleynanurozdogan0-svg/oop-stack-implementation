#Sınıf kullanarak yığın veri yapısı oluşturma
class Stack:
    def __init__(self,size):
        self.S=list()
        self.top=-1
        self.maxSize=size
        print("\n empty stack is created")
 
    def isFull(self):
        if(self.top==self.maxSize-1):
            return True
        else:
            return False
       
    def isEmpty(self):
        if(self.top<=-1):
            return True
        else:
            return False
       
    def push(self):
        if(self.isFull()==True):
            print("overflow: stack is full")
        else:
            no=int(input("enter the element to push"))
            self.top+=1
            self.S.insert(self.top,no)
            print("the element pushed is",no)
 
    def pop(self):
        if(self.isEmpty()==True):
            print("underflow: there is no element in the stack")
        else:
            print("the element popped is",self.S[self.top])
            self.top-=1
 
    def peek(self):
        if(self.isEmpty()==True):
            print("stack is empty")
        else:
            print("the element to peek is",self.S[self.top])
 
    def display(self):
        print("top is at index ->",self.top)
        if(self.isEmpty()==True):
            print("\n stack is empty")
        elif(self.isFull()==True):
            for i in range(self.top,-1,-1):
                print(i,"-->",self.S[i])
            print("\n stack is full")
        else:
            print("the elements in the stack is")
            for i in range(self.top,-1,-1):
                print(i,self.S[i])
 
 
def menu():
    print("\n------menu------")
    print("1. push an element")
    print("2. pop from stack")
    print("3. peek from stack")
    print("4. display the stack")
    print("5. exit")
    opt=int(input("enter a valid menu item....."))
    return opt
 
 
size=int(input("enter the size of the stack"))
St=Stack(size)
i=1
while(i>0 and i<5):
    i=menu()
    if(i==1):
        St.push()
        St.display()
    elif(i==2):
        St.pop()
        St.display()
    elif(i==3):
        St.peek()
        St.display()
    elif(i==4):
        St.display()
    else:
        print("exit")
 