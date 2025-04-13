from functools import reduce
l = [111, 2, 45, 55, 678, 74, 88]

def greater(a, b):
    if(a>b):
        return a
    else:
        return b
    
print(reduce(greater, l))