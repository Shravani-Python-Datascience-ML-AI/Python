

def Factsum(No):
    sum = 0
    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i

            print("sum of fact",sum)


def main():
    print("enter the number")
    No = int(input())
    Factsum(No)


if __name__ == "__main__":
    main()
