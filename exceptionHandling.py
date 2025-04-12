try:
    a = int(input("Enter a number: "))
    print(a)

except ValueError as v:
    print("Invalid input! Please enter a valid number.")
    print(v)

except Exception as e:
    print(e)

print("End of program")

# Raise Error in Code

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if(b == 0):
    raise ZeroDivisionError("Division by zero is not allowed.")
else:
    print(f"The division of a/b is {a / b}")


# Q1.
try:
    with open("1.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)
try:
    with open("2.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)
try:
    with open("3.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)
    
print("Thank you")