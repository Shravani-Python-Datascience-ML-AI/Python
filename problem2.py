"""Iterate through the first 10 numbers (0–9). In each iteration, print the current number, 
   the previous number, and their sum."""

print("Printing current and previous number sum in a range(10)")
previous_num = 0


for i in range(10):
    sum = previous_num + i
    print("Current Number", i, "Previous Number", previous_num, "Sum:", sum)
    
    
    previous_num = i