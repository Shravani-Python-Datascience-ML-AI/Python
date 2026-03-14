



def main():
    print("enter the number")
    n=int(input())
    Sum=0
    while(n>0):
        digit =n%10
        Sum=Sum+digit
        n=n//10
    print("The total sum of digits is:",Sum)

if __name__ == "__main__":
    main()