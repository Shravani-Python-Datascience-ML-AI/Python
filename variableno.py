def Add(*values):
    Sum = 0


    for no in values:
        Sum = Sum +no


        return Sum

def main():
    Ans = Add(1,7,9,4,5)
    print("Addition",Ans)


if __name__ == "__main__":
    main()

