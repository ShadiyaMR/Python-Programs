#square the list of numbers
# x=[2,9,5,1,7]
# y=list(map(lambda z:z**2,x))
# print(y)

#double the list of numbers
# a=[5,3,8,6,2]
# x=list(map(lambda y:y*2,a))
# print(x)

#find even numbers in a list
# x=[8,10,5,2,3,7,13,1,15]
# a=list(filter(lambda b:b%2==0,x))
# print(a)

#square the even numbers in a list
# a=[2,4,3,6,1,10]
# x=list(filter(lambda y:y%2==0,a))
# print(x)
# z=list(map(lambda b:b**2,x))
# print(z)

#double the odd numbers only
# a=[4,2,3,9,7,1,6]
# x=list(filter(lambda y:y%2!=0,a))
# print(x)
# z=list(map(lambda b:b*2,x))
# print(z)

#calculate the length of the string in a list
# a=["red","green","blue","yellow","pink"]
# x=list(map(lambda y:len(y),a))
# print(x)

#find the negative numbers in a list
a=[3,-6,-7,5,8,-1,6,]
x=list(filter(lambda y:y<0,a))
print(x)