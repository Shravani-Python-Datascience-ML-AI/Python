def SumFact(no):

    i = 1
    sum =0
    while i<no:
        if no%i == 0:
            sum = sum +i

        i = i+1
    print(sum)

def main():
    print("enter the number")
    no = int(input())
    SumFact(no)

if __name__ == "__main__":
    main()
