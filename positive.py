

def Check(No):

    if No == 0:
        print("Zero")
    elif No > 0:
        print("positive")
    else:
        print("Negative")

def main():

    print("enter the number")
    No = int(input())
    Check(No)

if __name__ == "__main__":
    main()
