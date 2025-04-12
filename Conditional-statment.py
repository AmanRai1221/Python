a=300
b=400

# if a>b:
#     print("a is greater than b")    
# elif a==b:
#     print("a is equal to b")
# else:
#     print("b is greater than a")

# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("a1 is greater",a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#     print("a2 is greater",a2)

# elif(a3>a2 and a3>a1 and a3>a4):
#     print("a3 is greater",a3)

# elif(a4>a2 and a4>a1 and a4>a3):
#     print("a4 is greater",a4)

# 3. Write a program to calculate the percentage.
marks1 = int(input("Enter your marks: "))
marks2 = int(input("Enter your marks: "))
marks3 = int(input("Enter your marks: "))

total_percentage = ((marks1 + marks2 + marks3)/300)*100

if (total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You have passed the exam",total_percentage)
else:
    print("You failed, Better Luck next time",total_percentage)

# Chapter 6