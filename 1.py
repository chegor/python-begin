a = [int(i) for i in input().split()]
final = []
widtha = len(a)
if len(a) == 1:
    print (a[0])



else:
    i = 0
    for x in a:
        if i == 0:
            firstsum = a[i+1] + a[widtha - 1]
            final.append(firstsum)

            i +=1
        elif i < widtha - 1:
            othersum = a[i+1] + a[i-1]
            final.append(othersum)

            i +=1
        elif i == len(a) - 1:
            lastsum = a[i-1] + a[0]
            final.append(lastsum)


for j in final:
    print (j, end=' ')
