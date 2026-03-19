
def year_fxn(n):
    if n%4==0 and  n%100 != 0:
        print("Leap year")
    else:
        print("Non leap year")   


n=int(input("Enter the year"))
year_fxn(n)