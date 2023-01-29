num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
def addition(num1,num2):
    num1+=num2
    return num1
def subtraction(num1,num2):
    num1-=num2
    return num1
def multiplication(num1,num2):
    num1*=num2
    return num1
def division(num1,num2):
    num1/=num2
    return num1
def module(num1,num2):
    num1%=num2
    return num1
def floordivision(num1,num2):
    num1//=num2
    return num1
def default(num1,num2):
    return "Wrong one"
switcher={1:addition,2:subtraction,3:multiplication,4:division,5:module,6:floordivision}
def switch(operation,num1,num2):
    return switcher.get(operation,default)(num1,num2)
print("Choose your choice to perform operations 1. addition 2. subtraction 3. multiplication 4. division 5. Module 6. Floordivision")
choice=int(input("Select operation from 1,2,3,4,5,6:"))
print(switch(choice,num1,num2))
