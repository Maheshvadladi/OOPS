#OOPS (Object Oriented Programming)
#1. A class contains attributes or variables and methods and functions that can manplucate the data.
#2. A class is the blueprint of an object.
#3. An object is an initation of a class.
#4. Methods or functions define inside the body of the class.

#oops syntax
'''class classname():
    name="codegnan"
    age=2018
    place="vja"
    def fname(method):
        print(statements.......)
a=classname()
print(dir(a))
a.fname()'''

#class declaration
'''class Details():
    name="pooja"
    age=27
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#object instantiation
'''class Details:
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def Display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Data("kowshik",23,"vja")
a.Display()
b=Details()
b.Data("mahesh",23,"vja")
b.Display()'''

#object initialization
'''class Details:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def Display(self):
        print(self.name,self.age,self.place)
a=Details("simhadri",98,"vja")
a.Display()
b=Details("mohit",100,"hyd")
b.Display()'''

#run time
'''class Details:
    name=input("enter name: ")
    age=int(input("Enter age: "))
    def display(self):
        print(self.name,self.age)
a=Details()
a.display()'''

#1st method
'''class Details:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def Display(self):
        print(self.name,self.age,self.place)
a=Details(input("Enter name: "), int(input("Enter age: ")), input("Enter place: "))
a.Display()'''

'''class Details:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def Display(self):
        print(self.name,self.age,self.place)
name=input("enter name: ")
age=int(input("Enter age: "))
place=input("Enter place: ")
a=Details(name,age,place)
a.Display()'''

#2nd method
'''class Details:
    def __init__(self):
        self.name=input("Enter name: ")
        self.age=int(input("Enter age: "))
        self.place=input("Enter place: ")
    def Display(self):
        print(self.name,self.age,self.place)
a=Details()
a.Display()'''
