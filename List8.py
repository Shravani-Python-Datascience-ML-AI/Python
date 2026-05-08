"""Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1) """

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Add a fruit to the end
fruits.append("fig")

# Remove the second fruit (index 1)
fruits.pop(1)

print(fruits)