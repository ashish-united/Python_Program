def Armstrong(a):
    a_str = str(a)
    b = len(a_str)
    d = a
    e = 0
    while d > 0:
        c = d % 10
        e = e + c ** b
        d = d // 10
    if e == a:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")


def Reverse(a):
    x = 0
    while a > 0:
        z = a % 10
        x = x * 10 + z
        a = a // 10
    print("Reverse is " + str(x))


a = int(input("Enter the Number: "))
b = int(input("1.Armstrong 2.Reverse: "))
if b == 1:
    Armstrong(a)
elif b == 2:
    Reverse(a)
else:
    print("Invalid choice")


