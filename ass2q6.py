# This program checks the strength of a password based on given criteria
      # i) At least 8 characters 
      # ii) Must contain capital and lower-case character 
      # iii) Must contain symbol and digit 

password = input("Enter password: ")

# Flags for conditions
has_upper = False
has_lower = False
has_digit = False
has_symbol = False

symbols = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"

# Loop through each character
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in symbols:
        has_symbol = True

# Final check
if len(password) >= 8 and has_upper and has_lower and has_digit and has_symbol:
    print("Strong password")
else:
    print("Weak password")