class Employee:
    language = "Python"  # This is Class attribute
    language = "Java"
    salary = 12000


# def getInfo(self):
#     print(f"The language is {self.language}. The salary is {self.salary}")

# def greet(self):
#     print("Good Morning")

# harry = Employee()
# harry.greet()
# harry.getInfo()

# This is a constructor method
def __init__(self):  #Dunder method
    print("Constructor is called")


harry = Employee()
harry.name = "Harry"
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan"
rohan.salary = 15000   # This is Instance attribute
print(rohan.name, rohan.salary, rohan.language) 

# Q1 Create a Class that stores programmer details working at Microsoft
class Programmer:
    company = "Microsoft"  # Class attribute
    def __init__(self, name, salary, pin):
        self.name = name  # Instance attribute
        self.salary = salary
        self.pin = pin

p = Programmer("Harry", 10000, 1234)
print(p.name,p.salary, p.pin, p.company)
r = Programmer("Rohan", 15000, 5678)
print(r.name,r.salary, r.pin, r.company)

# Q3. Create a class Calculator that takes a number and has methods to calculate square, cube and square root of the number
class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The square is {self.n**1/2}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()

# Q4. 
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"Ticket booked from {fro} to {to} in train no: {self.trainNo}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(200, 4000)}")
t = Train(12399)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")