# a=open("fruits.txt","x")
a=open("fruits.txt","w")
a.write("apple")
a.write("\norange")
a.close()
a=open("fruits.txt","a")
a.write("\nbanana")
a.close()
a=open("fruits.txt","r")
print(a.read())
a.close()
a=open("fruits.txt","r")
print(a.read(3))
a.close()
a=open("fruits.txt","r")
print(a.readline())
print(a.readline())
# y=open("colors.txt","x")
import os
# os.remove("colors.txt")
os.rmdir("shadiyaa")