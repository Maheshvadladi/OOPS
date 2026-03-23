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

#difference b/w _ and __
#We generally use it for private variables, that means whenever we use double leading underscore for a variable our python interpreter
#treats it as a special variable in order to avoid main conflicts with methods in inner classes.

'''class Employee():
    def __init__(self):
        self.name="mahesh"
        self._mailid="m@gmail.com"
        self.__salary=10000
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary) Error
print(a._Employee__salary)'''

'''class Employee():
    def __init__(self):
        self.name1="mahesh"
        self.mailid1="m@gmail.com"
        self.__salary1=100000
        self.name2="manoj"
        self.mailid2="mn@gmail.com"
        self.__salary2=500000
a=Employee()
print(dir(a))
print(a.name1, a.name2)
print(a.mailid1, a.mailid2)
print(a._Employee__salary1, a._Employee__salary2)'''

'''class Employee1():
    def __init__(self):
        self.name1="mahesh"
        self.mailid1="m@gmail.com"
        self.__salary1=100000
class Employee2():
    def __init__(self):
        self.name2="manoj"
        self.mailid2="mn@gmail.com"
        self.__salary2=500000
a=Employee1()
b=Employee2()
print(a.name1, b.name2)
print(a.mailid1, b.mailid2)
print(a._Employee1__salary1, b._Employee2__salary2)'''

