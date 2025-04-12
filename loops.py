l = [1, "Aman", False, "this", "Rohan", "Shubham"]

i = 0
while(i<len(l)):
    print(l[i])
    i += 1

# For Loop
for i in range(5):
    print(i)

# For loop in List
l = [1, 4, 678, 3, 9]
for i in l:
    print(i)

# For loop in String
s = "Harry"
for i in s:
    print(i)

# For loop in Tuple
t = {6, 3, 45, 89}
for i in t:
    print(i)

# For loop in Dictionary
d = {"a": 1, "b": 2, "c": 3}
for i in d:
    print(i, d[i])

# Nested For Loop
for i in range(5):
    for j in range(5):
        print(i, j)

for i in range(10):
    if(i == 5):
        break
    print(i)

for i in range(10):
    pass # Pass for future use.

for i in range(10):
    if(i == 5):
        continue
    print(i)

# Problems Questions Chapter 7

# 1. Write a program to print the multiplication table of a number entered by the user.
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 2.
l = ["Harry", "Sohan", "Sachin","Rahul"]
for name in l:
    if (name.startswith("S")):
        print(f"Hello {name}")

# 3.
n = int(input("Enter the number: "))
i = 1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i += 1

# 4.Prime Number
n = int(input("Enter the number: "))
for i in range(2, n):
    if(n%i == 0):
        print("Number is not prime")
        break
else:
    print("Number is prime")

# 5.
n = int(input("Enter the number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i += 1
print(sum)

# 6.Factorial of a number
n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i
print(f"The factorial of {n} is {product}")

# 7. Pattern
#   *
#  ***
# *****
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print("")

# 8. Pattern print i times
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print("*"*i, end="")
    print("")

# 9.Box Pattern
n = int(input("Enter the number: "))
for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")

# Reverse Table
# n = int(input("Enter the number: "))
# for i in range(10, 0, -1):
#     print(f"{n} x {i} = {n*i}")

n = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{n} X {11 - i} = {n*(11-i)}")