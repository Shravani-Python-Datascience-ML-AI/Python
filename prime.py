


def Prime(no):
    flag = False
    for i in range(2,no):
        if(no % i) == 0:
            flag = True
            break


    if flag:
        print("it is not a prime no",no)
    else:
        print("it is a prime no",no)


def main():
   print("enter the number")
   no = int(input())
   Prime(no)

if __name__ == "__main__":
    main()