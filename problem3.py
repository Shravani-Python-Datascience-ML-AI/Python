""" Display only those characters
 which are present at an even index number in given string."""

word = input("Enter the string: ")
print("Original String is", word)

even_char = word[0::2]

for char in even_char:
    print(char)
