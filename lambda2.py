def main():


    MultiplicationFunction = lambda No1,No2: No1*No2

    print("enter the first  number")
    No1 = int(input())
    print("enter the second number")
    No2 = int(input())
    Ans = MultiplicationFunction(No1,No2)


    print("Multiplication of number  using lambda function : ",Ans)


if __name__ == "__main__":
    main()
