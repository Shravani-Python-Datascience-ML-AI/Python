# write a program which contains fun ChkNum() which accept one parameter as number if
#the number is even display even otherwise display odd

def ChkNum(No):
    if(No % 2 == 0):
        print("no is even")
    else:
        print("no is odd")

def main():
    print("enter the no")
    No = int(input())

    ChkNum(No)

if __name__ == "__main__":
    main()

