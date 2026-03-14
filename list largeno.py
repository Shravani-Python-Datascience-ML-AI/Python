def large(Arr):
    large= Arr[0]
    for i in Arr:
        if i>large:
            large=i
    return large

def main():

    list=[]
    print("Enter size of list")
    size= int(input())
    for i in range(0,size):

        values=int(input("Enter element of list "))

        list.append(values)


    print("Largest is")
    print(large(list))

if __name__ == "__main__":
    main()