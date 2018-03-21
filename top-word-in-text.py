a = input().lower().split()
max_a = max([a.count(i) for i in set(a)])
c = {i: a.count(i) for i in set(a) if a.count(i) == max_a}
print(sorted(c)[0],c[sorted(c)[0]])