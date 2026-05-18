

print("Accept numbers from a user")
def Multiplication(No1,No2):
   Ans = No1 * No2
   return Ans


def main():
    print("enter first number:")
    Value1 = int(input())

    print("enter second number:")
    Value2 = int(input())

    Ans = Multiplication(int(Value1),int(Value2))
    print("Multiplication is:",Ans)
if __name__ == "__main__":
    main()