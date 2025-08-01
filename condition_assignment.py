#a=int(input("enter a number"))
#b=int(input("enter a number"))
#c=int(input("enter a number"))
#if a>=b and a>=c:
#print("the largest number is a")
#elif b>=a and b>=c:
#print("the largest number is b")
#else:
#print("the largest number is c")

a=int(input("enter a number"))
b=int(input("enter a number"))
c=input("enter a operation")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
else:
    print(a/b)