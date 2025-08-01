a={"name":"shadiya","age":22,"gender":"female","place":"ernakulam"}
print(a)
print(type(a))
print(len(a))
print(a["age"])
print(a.get("gender"))
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
print("age"in a)
print("age"not in a)
a["age"]=25
print(a)
a.update({"age":24})
print(a)
a["state"]="kerala"
print(a)
a.update({"country":"india"})
print(a)
b=a.copy()
print(b)
c=dict(a)
print(c)
a.pop("place")
print(a)
a.popitem()
print(a)
del a["gender"]
print(a)
a.clear()
print(a)
del a
family={
    "child 1":{"name":"rahul","age":12},
    "child 2":{"name":"ram","age":10},
    "child 3":{"name":"rohit","age":5}
    }
print(family)
print(family["child 2"])
print(family["child 2"]["age"])