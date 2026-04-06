print("Enter marks of all five Subject")
a=int(input("Enter the marks of physics "))
b=int(input("Enter the marks of math "))
c=int(input("Enter the marks of hindi "))
d=int(input("Enter the marks of english "))
e=int(input("Enter the marks of biology "))
total=a+b+c+d+e
average=total//5
print("Physics =",a)
print("Math =",b)
print("Hindi =",c)
print("English =",d)
print("Biology =",e)
print("Average Number =",average)
print("Total Number =",total)
if(average>80):
    print("Grade A")
elif(average>60):
    print("Grade B")
elif(average>40):
    print("Grade C")
else:
    print("Fail")

