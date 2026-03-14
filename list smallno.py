def small(Arr):
    small= Arr[0]
    for i in Arr:
        if i < small:
            small = i
    return small

def main():

    list=[]
    print("Enter size of list")
    size= int(input())
    for i in range(0,size):
        values=int(input("Enter element of list "))
        list.append(values)


    print("smallest is is")
    print(small(list))

if __name__ == "__main__":
    main()