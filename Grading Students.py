grade = [73, 45, 78, 15, 65, 38, 35, 36, 48, 75, 96, 12, 45, 62]
grade2 = []
for i in grade:
    if i >= 38 and i % 5 == 0:
        # print(i, end=" ")
        grade2.append(i)
    elif i >= 38:
        r = int(i/5)
        r = r+1
        a = r*5
        a = a-i
        if a <3:
            i = i+a
            # print(i, end=" ")
            grade2.append(i)
        elif a >= 3:
            # print(i,end=" ")
            grade2.append(i)
    else:
        # print(i,end=" ")
        grade2.append(i)
print(grade2)


