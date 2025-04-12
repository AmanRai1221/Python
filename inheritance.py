class Employee:  #Base class
    company = "Google"  # Class attribute
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):   #Derived class
    company = "Microsoft"
    def showLanguage(self):
        print(f"The language is {self.language}")

a = Employee()
b = Programmer()

print(a.company, b.company)


# Multiple Inheritance
class Employee:  #Base class
    company = "Google"  
    name = "Harry"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"The language is {self.language}")

class Programmer(Employee, Coder):   #Derived class
    company = "Microsoft"
    def showLanguage(self):
        print(f"The language is {self.language} and company is {self.company}")

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()


# Multilevel Inheritance
class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)