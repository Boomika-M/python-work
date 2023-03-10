def isempty(Que):
    if Que==[]:
        return True
    else:
        return False
def Enqueue(Que):
    ele=int(input("Enter the element to be Enqueued:"))
    Que.append(ele)
    if len(Que)==1:
        front=rear=0
    else:
        rear=len(Que)-1
    print(ele,"Enqueued")
def Dequeue(Que):
    if isempty(Que):
        print("Under flow!Queue is Empty")
    else:
        val=Que.pop(0)
        if len(Que)==0:
            rear=front=None
        print(val,"Dequeued")
def peek(Que):
    if isempty(Que):
        print("Under flow!Queue is Empty!No value at Front")
    else:
        front=0
        print("Front element is the Queue=",Que[front])
def display(Que):
    if isempty(Que):
        print("Queue Empty")
    else:
        print("Queue Elements:",Que)
Que=[]
front=rear=None
while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit\n")
    choice=int(input("Enter the choice:"))
    if choice==1:
        Enqueue(Que)
    elif choice==2:
        Dequeue(Que)
    elif choice==3:
        peek(Que)
    elif choice==4:
        display(Que)
    else:
        break