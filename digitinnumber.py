



def main():
    n=int(input("Enter number:"))
    cnt =0
    while(n>0):
        cnt=cnt+1
        n=n//10
    print("The number of digits in the number are:",cnt)

if __name__ == "__main__":
    main()