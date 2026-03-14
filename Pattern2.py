




def main():
    print("enter the rows ")
    rows = int(input())
    for i in range(rows,0,-1):
        for j in range(0,i):
            print("* ",end="")
        print("\n")

if __name__ == "__main__":
    main()




