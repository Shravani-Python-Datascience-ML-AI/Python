print("Apllication to demonstrate industrial programming")
def Addition(Value1,Value2):
    Ans = Value1 + Value2
    return Ans
def main():
    print("enter first number:")
    no1 = int(input())
    print(type(no1))
    print("enter second number:")
    no2 = int(input())
    print(type(no1))
    Sum = Addition(no1,no2)
    print("additon is:",Sum)
if __name__ == "__main__":
    main()