a={"fruit":"apple","color":"red","animal":"cat","bird":"crow"}
print(a)
print(type(a))
print(len(a))
print(a["animal"])
print(a.get("color"))
print(a.keys())
print(a.values())
print(a.items())
for i in a:
    print(i)
for i in a:
    print(a[i])
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
a["state"]="kerala"
print(a)
b=a.copy()
print(b)
c=dict(a)
print(c)
a.pop("bird")
print(a)
a.popitem()
print(a)
a.clear()
print(a)
del a
school={"std 1":{"name":"akhil","age":12},"std 2":{"name":"arjun","age":10}}
print(school)
print(school["std 1"])
print(school["std 1"]["age"])