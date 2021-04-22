x = input().split()
y = input().split()
l = []
for i in y:
    i = int(i)
    l.append(i)
l.sort()
l = l[:int(x[0])]
print(max(l)-min(l))
