
def main():


    SquareFunction = lambda No : No*No

    print("enter the number")
    No = int(input())
    Ans = SquareFunction(No)


    print("Square of  using lambda function : ",Ans)


if __name__ == "__main__":
    main()
