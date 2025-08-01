x={23,54,27,17,46,72}
print(x)
print(type(x))
print(len(x))
print(54 in x)
print(65 not in x)
for i in x:
    print(i)
x.add(79)
print(x)
y={16,35,11,28}
x.update(y)
print(x)
a={5,8,2,9,4,3}
b={4,2,7,1,6,8,3}
print(a)
print(b)
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)
x=a.difference(b)
print(x)
y=a.symmetric_difference(b)
print(y)
a.remove(2)
print(a)
a.discard(1)
print(a)
a.pop()
print(a)
a.clear()
print(a)
del a