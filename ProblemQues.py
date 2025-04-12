# 1. Write a program to calculate the sum of elements in a list.
a = int(input("Enter number: "))
b = int(input("Enter number: "))

print(a + b)

c = 39
d = 5
print("Remainder is: ",c % d)

# 2. Write a program to calculate the square of a number.
e = int(input("Enter number: "))
print("Squre is: ", e**2)
print("Squre is: ", e*e)

# 3. Write a program to calculate the sum of elements in a list.
marks = []
f1 = int(input("Enter Marks here: "))
marks.append((f1))
f2 = int(input("Enter Marks here: "))
marks.append((f2))
f3 = int(input("Enter Marks here: "))
marks.append((f3))
f4 = int(input("Enter Marks here: "))
marks.append((f4))
f5 = int(input("Enter Marks here: "))
marks.append((f5))
marks.sort()
print(marks)

l = [3, 5, 7, 4]
print(sum(l))

# Dict & Sets
# 1. Create a dictionary with 5 key-value pairs.
words ={
    "madad": "Help",
    "kursi": "Chair",
    "billi": "Cat"
}
word = input("Enter the word you want to meaning of: ")
print(words[word])

# 2. Create a set with 6 elements.
s = set()
n = input("Enter the number: ")
s.add(int(n))
n = input("Enter the number: ")
s.add(int(n))
n = input("Enter the number: ")
s.add(int(n))
n = input("Enter the number: ")
s.add(int(n))
n = input("Enter the number: ")
s.add(int(n))
n = input("Enter the number: ")
s.add(int(n))

print(s)

s = set()
s.add(18)
s.add("18")
print(s)

d = {}
name = input("Enter name: ")
language = input("Enter language name: ")
d.update({name: language})
name = input("Enter name: ")
language = input("Enter language name: ")
d.update({name: language})
name = input("Enter name: ")
language = input("Enter language name: ")
d.update({name: language})
print(d) # {'John': 'Python', 'Jane': 'Java', 'Bob': 'C++'}

# Chapter 6 Questions

# 1 write theprogram to calculate the marks of sudents and show Grade
marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"
print("Your grade is: ",grade)

# 2. Post problems
post = input("Enter the post: ")
if("Harry".lower() in post.lower()):
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")