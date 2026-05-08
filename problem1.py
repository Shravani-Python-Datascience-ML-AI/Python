""" Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, 
return their product; otherwise, return their sum."""

def multiplication_or_sum(num1,num2):
  
 product = num1*num2

 if product<= 1000:
   return product
 else:
   return num1+num2
 
result = multiplication_or_sum(20,30)
print("result:",result) 
result = multiplication_or_sum(50,60) 
print("result:",result) 
