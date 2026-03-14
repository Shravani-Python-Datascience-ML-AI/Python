def add(a,b):
    c = a+b
    return c
def sub(a,b):
    c = a-b
    return c
def mul(a,b):
    c = a*b
    return c

def main():
    print("enter the first number")
    a = int(input())
    print("enter the second number")
    b = int(input())
    add(a,b)
    sub(a,b)
    mul(a,b)

if __name__ =="__main__":
    main()