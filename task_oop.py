
# class Student():
#     name = 'Ivan'
#     groupNumber = '10A'
#     Age = 18


# def init(self,name,groupNumber,Age):
#     self.name = name
#     self.groupNumber = groupNumber
#     self.Age = Age


# def get_name(self):
#     return 'Imia',self.name

# def get_groupNumber(self):
#     return 'gruppa',self.groupNumber

# def get_age (self):
#     return self.Age,'let'

# def set_Name_Age (self,newname,newAge):
#     self.name = newname
#     self.Age = newAge 

# def set_groupNumber (self,new_groupNumber):
#     self.groupNumber = new_groupNumber    



# a=Student()

# print(a.set_groupNumber())








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

a = Student('Roni', 19, 'a1')
b = Student('Bron', 19, 'a1')
c = Student('Chelo', 19, 'a1')
d = Student('Demi', 19, 'a1')
e = Student('Kasym', 19, 'a1')


a.setGroupNumber(rwr1)