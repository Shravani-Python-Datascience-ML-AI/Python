


def main():
    list = []
    print("enter the size ")
    size = int(input())
    print("enter the values")

    for i in range(0,size):
        values = int(input())
        list.append(values)
    print("enter the elements u want to search")
    no = int(input())
    cnt = 0
    for i in range(0,size):
        cnt = cnt + 1
    print("frequency",cnt)


if __name__ == "__main__":
    main()
