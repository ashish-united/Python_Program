# Fibonacci series up to N terms
# Recursive Fibonacci function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print first N terms
N = int(input("Enter N: "))
for i in range(N):
    print(fibonacci(i), end=" ")
