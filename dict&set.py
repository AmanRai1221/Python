# empt_dict = {} # Empty dict
marks ={
    "John": 85,
    "Jane": 92,
    "Bob": 78,
    "Harry": 95
}
print(marks, type(marks))
print(marks.values())
print(marks.keys())
print(marks.items())

marks.update({"Hari": 89, "Ram": 98})
print(marks)

print(marks.get("Harry"))
print(marks["Harry"])

# marks.clear()

# e = set() # Empty set
s = {1, 2, 3, 4, 45, 56}
print(len(s), type(s))
print(s.remove)
print(s.clear)
print(s.pop)
s1 = {1, 6, 3, 5, 45, 56}
print(s.union(s1))
print(s.intersection(s1))

# Summary of Useful Dictionary Methods:
# clear()
# copy()
# get()
# pop()
# popitem()
# update()
# keys()
# values()
# items()
# setdefault()
# fromkeys()

# Chapter 5

words = {
    "madad": "Help",
    "kursi": "Chair",
    "billi": "Cat"
}

word = input("Enter the word you want to meaning of: ")
print(words[word])