


def small(Arr):
    small = Arr[0]
    for i in  Arr:
     if(i<small):
        small = i
     return small

def main():

    list = []
    print("enter the size")
    size = int(input())
    print("enter the values")
    for i in  range(0,size):
     values = int(input())
     list.append(values)
     print(small(list))

if __name__ == "__main__":
    main()