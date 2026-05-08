""" Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence."""

sentence = "Learning Python is fun!"
vowels = "aeiou"
count = 0

# Convert to lowercase to handle 'A' and 'a' equally
for char in sentence.lower():
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")      
