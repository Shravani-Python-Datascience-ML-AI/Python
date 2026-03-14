



def Divisible(No):

    if No % 5 == 0:
        print("no is divisible")
    else:
        print("no is not divisible")


def main():

    print("enter the number")
    No = int(input())
    Divisible(No)

if __name__ == "__main__":
    main()