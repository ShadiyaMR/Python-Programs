# a=open("file1.txt","x")
# a=open("file1.txt","w")
# a.write("my name is shadiya")
# a.close()
# a=open("file1.txt","r")
# b=a.read()

# c=open("file2.txt","x")
# c=open("file2.txt","w")
# c.write(b)
# c.close()
# c=open("file2.txt","r")
# print(b)


# # a=open("newfile1.txt","x")
# a=open("newfile1.txt","w")
# a.write("good morning")
# a.close()
# a=open("newfile1.txt","r")
# b=a.read()

# # c=open("newfile2.txt","x")
# c=open("newfile2.txt","w")
# c.write("have a nice day")
# c.close()
# c=open("newfile2.txt","r")
# d=c.read()

# # x=open("newfile3.txt","x")
# x=open("newfile3.txt","w")
# x.write(b+d)
# x.close()
# x=open("newfile3.txt","r")
# print(x.read())


# a=open("message1.txt","x")
a=open("message1.txt","w")
a.write("hello,shadiya")
a.close()
a=open("message1.txt","r")
b=a.read()

# c=open("message2.txt","x")
c=open("message2.txt","w")
c.write("welcome to python programming")
c.close()
c=open("message2.txt","r")
d=c.read()

# e=open("message3.txt","x")
e=open("message3.txt","w")
e.write(b+"\n"+d)
e.close()
e=open("message3.txt","r")
print(b+"\n"+d)