# String
name = "Harish"

print("Hello,",name)
print(name[0:4])
print(name[-4:-1])
print(name[:4])
print(name[1:])

print(len(name))
print(name.endswith("sh"))
print(name.startswith("Ha"))
print(name.capitalize())
print(name.split())
print(" ".join(name))
print(name.isalpha())
print(name.isdigit())
print(name.count("hello"))

# Escape sequences Character
text = "Hello\a"
print(text)  # May produce a sound depending on the system

text = "Hello\nWorld"
print(text)

text = "Hello\tWorld"
print(text)

text = "This is a backslash: \\"
print(text)

text = 'It\'s a great day!'
print(text)

text = "She said, \"Hello!\""
print(text)

text = "Hello\rWorld"
print(text)

text = "Hello\bWorld"
print(text)

text = "\U0001F600"
print(text)

name = input("Enter your name: ")
print(f"Goog Afternoon, {name}")

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Harry").replace("<|Date|>","12-August-2020"))

# Strings are immutable
name = "Harry is good  boy and "
print(name.find("  "))
print(name.replace("  ", " "))

# Lists
friends = ["Apple", "Orange", 5, 345.07, False, "Akash","Rohan"]
print(friends[0])
friends[0] = "Grapes" #Unlike Strings lists are mutable
print(friends[0])
print(friends[1:4])
friends.append("Harry")
print(friends)
friends.reverse() #reverse
print(friends)
# friends.sort() #sort
friends.insert(2, 38)
print(friends)

l1 = [1, 34, 56, 90, 12]
print(l1)
value = l1.pop(3)
print(value)
print(l1)

#  ## Tuple ##
# A tuple is an immutable (unchangeable) sequence of values, which can hold elements of any data type such as numbers, strings, or other objects. Tuples are similar to lists, but unlike lists, they cannot be modified after they are created (i.e., they are immutable)
# Example of a tuple with multiple elements
my_tuple = (1, 2, 3, 4)
print(my_tuple)
print(2 in my_tuple)
print(my_tuple[1])
print(my_tuple[-1])
print(len(my_tuple))

repeated_tuple = my_tuple * 3
print(repeated_tuple)

# Single element tuple (you need a trailing comma)
single_element_tuple = (5,)
print(single_element_tuple)

empty_tuple = ()
print(empty_tuple)

# Tuple with different data types
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)

# @@ Tuple vs List:
# Tuples are immutable, while lists are mutable.

# Tuples have a smaller memory footprint, and their elements are fixed once created.

# Lists are better suited when you need to modify the sequence (add, remove, or change elements), while tuples are used when the sequence should remain constant.