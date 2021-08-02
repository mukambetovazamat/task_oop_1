#task1

class Student:
    name = 'Ivan'
    age = 18
    groupNumber = '10A'

    def __init__(self, name, age, groupNumber):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, new_name, new_age): 
        self.name = new_name
        self.age = new_age

    def setGroupNumber(self, new_groupNumber): 
        self.groupNumber = new_groupNumber

a = Student('joni', 19, 'a1')
b = Student('Dep', 19, 'a1')
c = Student('Stiv', 19, 'a1')
d = Student('Ivan', 19, 'a1')
e = Student('Till', 19, 'a1')

#task2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def substraction(self):
        print(self.a - self.b)

num1 = Math(10, 5)
num1.addition()
num1.multiplication()
num1.division()
num1.substraction()

#task3
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    
    def turnOn(self):
        print('Car is on')

    def turnOff(self):
        print('Car is off')

    def setYear(self, new_year): 
        self.year = new_year

    def setType(self, new_type):
        self.type = new_type

    def setColor(self, new_color):
        self.color = new_color