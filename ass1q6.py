# Count vowels and their index positions

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for index, char in enumerate(text):
    if char in vowels:
        print(f"Vowel '{char}' found at index {index}")
        count += 1

print("Total number of vowels:", count)