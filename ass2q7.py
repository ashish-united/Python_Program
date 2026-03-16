# Check if number is prime Number is prime if it is greater than 1 and has no divisors other than 1 and itself

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not Prime Number")
            break
    else:
        print(num, "is Prime Number")
else:
    print(num, "is not Prime Number")