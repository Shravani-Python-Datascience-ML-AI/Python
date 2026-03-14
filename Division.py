


def div(a,b):
    ans = 0
    ans = a // b
    return ans
def fdiv(a,b):
    ans = 0
    ans = a / b
    return ans


def main():
    print("enter the number")
    a = int(input())
    print("enter the second number")
    b = int(input())
    division = div(a,b)
    print(division)
    floatdivision = fdiv(a,b)
    print(floatdivision)

if __name__ == "__main__":
    main()