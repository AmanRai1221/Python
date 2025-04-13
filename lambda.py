
# Lambda Function
# Lambda make veriable function, Variable that used like a Function.
# def square(n):
#     return n * n

square = lambda n: n * n
print(square(5))


# Join Method
a = ["Hello", "World", "Ram"]
# final = "-".join(a)
final = "::".join(a)
print(final)

# Format Function
# Format function is used to format the string.
a = "{0} is a good {1}".format("Python", "Language")
print(a)

# Map Example
# Map function is used to apply a function to all the items in an iterable (list, tuple etc.)
l = [1, 2, 3, 4, 5]
square = lambda n: n * n
sqlist = list(map(square, l))
print(sqlist)

# Filter Example
l = [1, 2, 3, 4, 5]
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Example
from functools import reduce

l = [1, 2, 3, 4, 5]
def sum(a, b):
    return a + b

mul = lambda a, b: a * b

print(reduce(sum, l))
print(reduce(mul, l))

# Q1.
from functools import reduce
l = [111, 2, 45, 55, 678, 74, 88]

def greater(a, b):
    if(a>b):
        return a
    else:
        return b
    
print(reduce(greater, l))