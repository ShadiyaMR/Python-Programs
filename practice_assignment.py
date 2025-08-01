#print the pattern
# a=5
# for i in range(1,a+1):
#     spaces = ' ' * (a - i) * 2
#     s = '* ' * i
#     print(spaces + s)

# a=5
# for i in range(5):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# for i in range(1,10,2):
#     print("*"*i)

#reverse a string using for loop
# x=input("enter a string")
# reverse=""
# for i in range(len(x)-1,-1,-1):
#     reverse+=x[i]
# print(reverse)

#Python program to check whether a year is leap year or not
year=int(input("enter a year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it is leap year")
        else:
            print("it is not leap year")
    else:
        print("it is leap year")
else:
    print("it is not leap year")


