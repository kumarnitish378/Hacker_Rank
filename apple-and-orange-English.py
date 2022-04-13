s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]
def appleOrange(s,t,a,b,apples,oranges):
    app_dist =[]
    org_dist =[]
    for i in apples:
        app_dist.append(a+i)
    for i in oranges:
        org_dist.append(b+i)
    apple = 0
    for i in app_dist:
        if i >= s and i <= t:
            apple = apple + 1
    orange = 0
    for i in org_dist:
        if i >= s and i <= t:
            orange = orange+1
    return (apple,orange)
# print(apple)
print(appleOrange(s,t,a,b,apples,oranges))
# print(orange)
