a={"jan","feb","march","april","may"}
print(a)
print(type(a))
print(len(a))
print("june"in a)
print("june"not in a)
for i in a:
    print(i)
a.add("june")
print(a)
b={"july","aug","sep"}
a.update(b)
print(a)
x={"oct","nov","dec","jan"}
y={"jan","feb","march"}
z=x.union(y)
print(z)
c=x.intersection(y)
print(c)
d=x.difference(y)
print(d)
e=x.symmetric_difference(y)
print(e)
x.remove("jan")
print(x)
x.discard("april")
print(x)
x.pop()
print(x)
x.clear()
print(x)
del x