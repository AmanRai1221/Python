# class Employee:
#     a = 1

#     def show(self):
#         print(f"The class attribute is {self.a}")

# e = Employee()
# e.a = 45
# e.show()

# classmethod show class attribute

# Encapsulation, Abstraction
class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Hari Prasad"
print(e.fname, e.lname)
e.show()

# Q1.
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(1, 2, 3)
b.show() 

# Q2.

class Animals:
    def eat(self):
        print("Animal is Eating...")
    

class Pets(Animals):
    def sleep(self):
        print("Pet is Sleeping...")
    

class Dog(Pets):

    @staticmethod
    def bark():
        print("Dog is barking...")
    
a = Animals()
a.eat()

p = Pets()
p.sleep()
# p.eat()

d = Dog()
d.bark()

# Q3.
class Employee:
    salary = 234
    inccrement = 20
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.inccrement/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.inccrement = ((salary/self.salary) - 1) * 100

e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280
print(e.inccrement)