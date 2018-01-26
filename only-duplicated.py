a = [int(i) for i in input().split()]
a.sort()
final = []

i = 0
for x in a:
    if (i != len(a)-1) and (x == a[i+1]):

        i += 1
    else:
        if (x == a[i-1]) and (len(a) != 1):
            final.append(x)
            i += 1
        else:
            i += 1

for j in final:
    print (j, end=' ')
