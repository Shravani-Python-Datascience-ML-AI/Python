

def main():

    list = []
    print("Enter size of list")
    size= int(input())
    for i in range(0,size):
        values=int(input("Enter element of list "))
        list.append(values)
    print("enter element you want to search")
    no = int(input())
    Cnt = 0
    for i in range(0,size):

            Cnt = Cnt + 1
    print("frequence :",Cnt)





if __name__ == "__main__":
    main()