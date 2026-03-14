#divisible by 5 or not

def Divisible(no):

    if no % 5 == 0:

        print("number is divisible by 5")

    else:

        print("number is not divisible by 5")


def main():

    print("enter the number")

    no = int(input())

    Divisible(no)

if __name__ == "__main__":

    main()

