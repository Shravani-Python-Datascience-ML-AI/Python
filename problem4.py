"""Write a function to remove characters from a
 string starting from index 0 up to n and return a new string."""
def remove_chars(word, n):
    print('Original string:', word)
    res = word[n:]
    return res

print("Removing characters from a string")
print(remove_chars("shravani", 4))
print(remove_chars("falguni", 2))
 

 