from functools import reduce

print("Demonstration of filter map reduce ")


def Evencheck(no):               # filter
    return(no % 2 == 0)
def increase(no):                # map
    return no+2
def Add(A,B):                  # reduce
    return A,B
arr = [8,9,5,16,2,4,21,30,11]
evenarr = list(filter(Evencheck,arr))
print("Data after filter",evenarr)
ModArray = list(map(increase,evenarr))
print("Data after map",ModArray)
sum = reduce(Add,ModArray)
print("Addition of even numbers",sum)

