lst = [int(i) for i in input().split()]
x = int(input())
final = []
y = 0
for i in lst:
    if i == x:
        final.append(y)
    y += 1

for i in final:
    print(i, end=' ')
if x not in lst:
    print('Отсутствует')