# Sum of digits using math
num = int(input("Enter a 5-digit number: "))
sum_digits = 0
temp = num

while temp > 0:
    d= temp%10
    sum_digits += d   
    temp = temp// 10              
    
print("Sum of digits:", sum_digits)