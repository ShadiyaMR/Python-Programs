# a=lambda x,y:x+y
# print(a(5,3))

# x=lambda a,b,c:a*b*c
# print(x(3,9,6))

# y=lambda a:a**2
# print(y(4))

a=["apple","banana","orange","cherry","guava"]
x=list(map(lambda y:y.upper(),a))
print(x)

x=[4,9,2,0,7,1]
b=list(filter(lambda a:a>5,x))
print(b)