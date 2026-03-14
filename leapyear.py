



def main():
    print("enter the year")
    year = int(input())
    if year % 4 == 0:
        print("is a leap year")
    elif year % 100 == 0:
        print("is not a leap year")
    elif year % 400 == 0:
        print("is a leap year")
    else:
        print("not a leap year")

if __name__ == "__main__":
    main()