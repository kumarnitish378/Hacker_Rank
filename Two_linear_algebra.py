order = int(input("enter order "))
# its produce wrong answer!!!
if order == 2:
    try:
        (a1,b1,c1) = map(int,input("enter 1st equation ").split())
    except:
        a1 = 0
        b1 = 0
        c1 = 0
    try:
        (a2, b2, c2) = map(int, input("enter 2nd equation ").split())
    except:
        a2 = 0
        b2 = 0
        c2 = 0
    try:
        y = ((a1*c2)-(b1*c1))/((a1*b2)-(a2*b1))
    except:
        y = 0
        pass
    print("value of y = {}".format(y))
    try:
        x = ((c1*b2)-(a2*c2))/((a1*b2)-(a2*b1))
    except:
        x = 0
        pass
    print("value of x = {}".format(x))
else:
    print("sorry i can not able to solve more than 2 equation!")