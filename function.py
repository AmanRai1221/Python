def goodDay(name, ending):
    print("Good Day," + name)
    print(ending)

goodDay("Harry", "Thank you")
goodDay("Mohan", "Thank you")
goodDay("Divya", "Thank you")

# factorial(n) = n*factorial(n-1)
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number: "))
print(f"The factorial of {n} is {factorial(n)}")

# 1. Find the greatest of three numbers using function.
def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = 2
b = 3
c = 4
print(greatest(a, b, c))

# 2.Find fahrenheit to celsius using function.
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter the temperature in Fahrenheit: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")

# 3.Write a program to prevent new line using print function.
print("a")
print("b")
print("c", end="")
print("d", end="")

# 4.Write a program to find the sum of first n natural numbers using function.

'''
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
..
sum(n)= sum(n-1) + n
'''
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(5))

# 5.Print pattern using recursion.
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
pattern(3)

# 6. To print inches to cm using function.
def inch_to_cm(inch):
    return inch * 2.54
n = int(input("Enter the value of inches: "))
print(f"The corresponding value in cm is {inch_to_cm(n)} cm")

def feet_to_cm(feet):
    return feet * 30.48
n = int(input("Enter the value of feet: "))
print(f"The corresponding value in cm is {feet_to_cm(n)} cm")

# 7. To remove a word from a list of strings using function.
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l = ["hello", "world", "Harry", "Rohan", "Shubham"]
print(rem(l, "an"))

# 8.Print the multiplication table of a number using function.
def multiply(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")
multiply(5)