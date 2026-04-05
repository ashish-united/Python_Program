def is_armstrong(num):
    # Convert number to string to count digits
    digits = str(num)
    power = len(digits)
    
    # Calculate sum of digits raised to the power
    total = sum(int(digit) ** power for digit in digits)
    
    return total == num

# Example usage
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")