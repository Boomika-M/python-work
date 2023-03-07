a=[]
n=int(input("Enter number of elements:"))
print("Enter element one by one")
for i in range(n):
    a.append(int(input()))
print("Unsorted list")
print(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print("After bubble sort:")
print(a)
    