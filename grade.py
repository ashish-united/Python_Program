# wap to input from user 5 number of subject and print the total , average , grade.
def grade_a(sum):
    sum=sum//5
    if(sum>=80):
        print("grade A")
    elif(sum>=60):
        print("grade B")
    elif(sum>=50):
        print("grade C")
    else:
        print("Fail")


a = int(input("Enter the 1st subject Number"))
b = int(input("Enter the 2nd subject Number"))
c = int(input("Enter the 3rd subject Number"))
d = int(input("Enter the 4th subject Number"))
e = int(input("Enter the 5th subject Number"))
grade_a(a+b+c+d+e)