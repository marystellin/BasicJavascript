class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.head
            self.head=newnode
            #print(singly)
    def insertend(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            self.tail.next=newnode
            self.tail=newnode
    def insertatpos(self,pos,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            temp=self.head
            for i in range(1,pos):
                temp=temp.next
                newnode=Node(value)
                newnode.next=temp.next
                temp.next=newnode
                #temp=None
    def delbeg(self):
        if(self.head==None):
            print("empty")
        else:
            temp=self.head
            self.head=temp.next
            temp=None
    def deleteend(self):
        if(self.head==None):
            print("empty")
        else:
            temp=self.head
            while(temp.next is not None):
                prev = temp
                temp = prev.next
            self.tail=prev
            self.tail.next=None



    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next

singly=SLL()
print("Welcome to singly linked list")
while(True):
    print("Which below operations need to be performed?")
    print("1.Insertion 2.Deletion 3.Searching 4.Updation 5.Display 6.Exit")
    n=input()
    if(n=="1"):
        print("CHOOSE YOUR OPTION")
        print("1. Insertion-at-beginning")
        print("2. Insertion-at-end")
        print("3. Insertion-at-any-position")
        n=int(input())
        if(n==1):
            print("Enter the first value")
            val=input()
            singly.insertatbeg(val)
        elif(n==2):
            print("Enter the last value")
            val=input()
            singly.insertend(val)
        elif(n==3):
            print("Enter the position")
            pos=int(input())
            print("Enter value to be inserted")
            val=input()
            singly.insertatpos(pos,val)
    elif(n=="2"):
        print("CHOOSE YOUR OPTION")
        print("1. Deletion at beginning")
        print("2. Deletion at end")
        print("3. Deletion at any position")
        n=int(input())
        if(n==1):
            singly.delbeg()
        elif(n==2): 
            singly.deleteend()
    elif(n==3):
            print("Enter value to be deleted")
            val=int(input())
            singly.delatpos(val)
        
    elif(n=="5"):
        singly.display()