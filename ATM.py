print("Welcome to State Bank of India")
p=int(input("Enter your four digit number:"))
m=25000
if(p==1234):
    print("1-Withdraw")
    print("2-Balance Enquiry")
    print("3-Fast Cash")
    c=int(input("Please choose your transaction mode:"))
    if(c==1):
        w=int(input("Enter the withdraw amount:"))
        if(w<m and w%100==0):
            print("Please take your amount:",w)
        else:
            print("Invalid cash")
    elif(c==2):
        print("Your available amount:",m)
    elif(c==3):
        print("1->5000")
        print("2->10000")
        print("3->15000")
        print("4->20000")
        f=int(input("Enter fash cash option:"))
        if(f==1 and 5000<m):
            print("Please take cash 5000")
        elif(f==2 and 10000<m):
            print("Please take cash 10000")
        elif(f==3 and 15000<m):
            print("Please take cash 15000")
        elif(f==4 and 20000<m):
            print("Please take cash 20000")
        else:
            print("Invalid fast cash option")
    else:
        print("Wrong choice")
else:
    print("Wrong Pin Number")
       