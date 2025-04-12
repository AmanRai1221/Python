l = [3, 45, 234, 6]

# index = 0
# for item in l:
#     print(f"The item at index {index} is {item}")
#     index += 1

# The above code can be simplified using the "enumerate function".

for index, item in enumerate(l):
    print(f"The item at index {index} is {item}")


# Q2. 
l = [1, 2, 3, 4, 5, 6, 7, 8]
for i, item in enumerate(l):
    if i ==2 or i == 4 or i == 6:
        print(item)

# Q3.
n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)

# Q4.
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError as e:
    print("Infinite")

# Q5.
n = int(input("Enter a number: "))
table = [n*i for i in range(1, 11)]
with open("table.txt", "a") as f:
    f.write(f"Table of {n}:{str(table)}\n")