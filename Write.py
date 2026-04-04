#Writing into File
f=open("data.txt","w")
age=int(input("Enter your Age :"))
Name=input("Enter your Name :")
Section=input("Enter Your Secion Long With Semster :")
f.write(str(age)+"\n")
f.write(Name+"\n")
f.write(Section+"\n")
f.close()
#Reading File
f=open("data.txt","r")
g=f.read()
print(g)
#Adding Some More Data Into File
f=open("data.txt","a")
data=input("Enter Any Set Of Instruction")
f.write(data)
#Again Printing the data
f=open("data.txt","r")
g=f.read()
print(g)


