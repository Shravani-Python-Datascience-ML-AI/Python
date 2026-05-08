# using third variable(temp) 

def swap(a,b):

    print("before swapping:",a,b)

    temp = 0
    temp = a,
    a = b,
    b = temp

    print("after swapping",a,b)
    return a,b

swap(5,6)