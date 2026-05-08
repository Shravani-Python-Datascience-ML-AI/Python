def swap(a, b):
    print("Before swap:", a, b)
    
    a, b = b, a   
    
    print("After swap:", a, b)
    return a, b


swap(5, 6)