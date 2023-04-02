import random
def test_exceptions():
    exception_type=random.randint(1,4)
    if exception_type==1:
        a=1/0
    elif exception_type==2:
        a=[1,2,3]
        print(a[3]) 
    elif exception_type==3:
        print(b)
    else:
        a='hello'
        b=2
        print(a+b)
try:
    test_exceptions()
except ZeroDivisionError:
    print("It is a zerodivision error")
except IndexError:
    print("It is a index error")
except NameError:
    print("It is a Name error")
except TypeError:
    print("It is type error")  