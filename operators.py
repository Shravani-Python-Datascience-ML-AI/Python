def add(a,b):
    ans = 0
    ans= a+b
    return ans
def sub(a,b):
    ans = 0
    ans = a-b
    return ans
def mul(a,b):
    ans = 0
    ans = a*b
    return ans

def main():
    print("enter the first number")
    a = int(input())
    print("enter the second number")
    b = int(input())
    addition = add(a,b)
    print(addition)
    substraction = sub(a,b)
    print(substraction)
    multiplication = mul(a,b)
    print(multiplication)

if __name__ =="__main__":
    main()