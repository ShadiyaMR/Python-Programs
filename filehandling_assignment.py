# a=open("birds.txt","x")
a=open("birds.txt","w")
a.write("crow")
a.write("\nparrot")
a.close()
a=open("birds.txt","a")
a.write("\nduck")
a.close()
a=open("birds.txt","r")
print(a.read())
a.close()
a=open("birds.txt","r")
print(a.read(6))
a.close()
a=open("birds.txt","r")
print(a.readline())
print(a.readline())
a.close()
# y=open("colors.txt","x")
import os
# os.remove("colors.txt")
os.rmdir("images")