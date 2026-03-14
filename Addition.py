



def Addition(No1,No2):
    Ans = 0
    Ans = No1+No2
    return Ans

def main():
    print("Enter the first no")
    No1 = int(input())
    print("enter the second number")
    No2 = int(input())
    Sum = Addition(No1,No2)
    print("Addition is",Sum)


if __name__ == "__main__":
     main()
