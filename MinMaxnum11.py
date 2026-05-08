#Given a list of integers, find and print both the largest and the smallest numbers

data= [45, 2, 89, 12, 7]
a = data[0]
b = data[0]

for x in data:
    if x < a:
        a = x
    if x > b:
        b = x

print("Min value:", a)
print("Max value:", b)
