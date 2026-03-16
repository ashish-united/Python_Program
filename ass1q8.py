# Check if a string contains a given letter and count occurrences
     # String given ='I am in Python.'
     # Output: Occur 2 time in string .


text = input("Enter a string: ")
letter = input("Enter the letter to search: ")

count = 0
for char in text:
    if char == letter:
        count += 1

if count > 0:
    print(f"Letter '{letter}' occurs {count} time(s) in the string.")
else:
    print(f"Letter '{letter}' does not occur in the string.")