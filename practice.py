



def div(a,b):
    ans = 0
    ans = a//b
    return ans
def fdiv(a,b):
    ans = 0
    ans = a/b
    return ans

def main():
    print("enter the values")
    print("enter value of 'a' ")
    a = int(input())
    print("enter value of 'b' ")
    b = int(input())
    division = div(a,b)
    Floatdivision = fdiv(a,b)
    print(division)
    print(Floatdivision)


if __name__ == "__main__":
    main()