
def Addition(no1,no2):
    ans = 0
    ans = no1 + no2
    return ans

def main():
    print("enter the first number")
    no1 = int(input())
    print("enter the second number")
    no2 = int(input())
    sum = Addition(no1,no2)
    print("Addition is",sum)

if __name__ == "__main__":
    main()

