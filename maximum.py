print("Apllication to find maximum no")
def Maximum(No1,No2):
    if No1 > No2:
        return No1
    else:
        return No2


def main():
    print("enter first number:")
    Value1 = int(input())

    print("enter second number:")
    Value2 = int(input())

    Ans = Maximum(int(Value1),int(Value2))
    print("Maximum  is:",Ans)
if __name__ == "__main__":
    main()