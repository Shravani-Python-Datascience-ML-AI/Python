def CheckList(No):
    return (No >= 70 | No <= 90)

def Increment(No):
    return No+10

def filterX(Arr,CheckList):
    Result = []
    for no in Arr:
        if(CheckList(no)):
            Result.append(no)
    return Result

def mapX(Arr,Increment):
    Result = []
    for no in Arr:
        value = Increment(no)
        Result.append(value)
    return Result

def reduceX(Arr):
    Mul = 1
    for no in Arr:
        Mul= Mul * no
    return Mul

def main():
    Arr = list()
    print("Enter how many elements you want to store?")
    size = int(input())

    print("Please enter the values")

    for i in range(0,size):
       no = int(input())
       Arr.append(no)




    print("Original data : ",Arr)

    Data_Filter = list(filterX(Arr,CheckList))

    print("Data after filter : ",Data_Filter)

    Data_map = list(mapX(Data_Filter,Increment))

    print("Data after map : ",Data_map)

    Ret = reduceX(Data_map)

    print("Data after reduce : ",Ret)

if __name__ == "__main__":
    main()