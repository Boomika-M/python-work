num=int(input("Enter the number:"))
while num<=0:
    num=int(input("Enter the positive number:"))
else:
    sum=0
    for i in range(1,num+1):
        sum=sum+i
print("Sum of",num,"natural numbers is",sum) 