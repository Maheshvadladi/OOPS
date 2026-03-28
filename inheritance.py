#Inheritance
#single inheritance
'''class RBI( ):#parent class
    cash=100000
    def available_cash(cls):
        print("available cash is: ",cls.cash)
        print("available cash is: ",RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash=50000
    def new_cash(cls):
        print("new cash is: ",cls.cash+cls.cash)
        print("new cash is: ",RBI.cash+HDFC.cash)
a=HDFC( )
a.available_cash( )
a.new_cash( )'''

#child 2 to child 1
'''class RBI( ):#parent class
    cash=100000
    def available_cash(cls):
        print("available cash is: ",cls.cash)
        print("available cash is: ",RBI.cash)
class SBI(RBI):#child 1 to child 2 is not possible
    cash=30000
    def balance_cash(cls):
        print("balance_cash is: ",cls.cash+cls.cash)
        print("balance cash is: ",RBI.cash+SBI.cash)
class HDFC(SBI):#child 2 to child 1
    cash=50000
    def new_cash(cls):
        print("new cash is: ",cls.cash+cls.cash)
        print("new cash is: ",SBI.cash+HDFC.cash)
a=HDFC( )
a.available_cash( )
a.new_cash( )
b=SBI( )
b.available_cash( )
b.balance_cash( )'''

#multiple inheritance

'''class Father( ):
    weight=75
    def father_weight(cls):
        print("father weight is: ",cls.weight)
        print("father weight is: ",Father.weight)
class Mother( ):
    height=165
    def mother_height(cls):
        print("mother height is: ",cls.height)
        print("mother height is: ",Mother.height)
class Kid(Father,Mother):
    Dob="10-04-2004"
    def kid_age(cls):
        print("kid age is: ",cls.Dob)
        print("kid age is: ",Kid.Dob)
a=Kid( )
a.father_weight( )
a.mother_height( )
a.kid_age( )'''

#multi-level inheritance
'''class Grandfather( ):
    def Grandfather_land(self):
        print("grandfather have 10 acres land")
class Parent(Grandfather):
    def parent_house(self):
        print("Grandfather gave 2 houses to my parents")
class Child(Parent):
    def child_inh(self):
        print("My father gave me car")
a=Child( )
a.Grandfather_land( )
a.parent_house( )
a.child_inh( )'''

#task
'''class Dog_Breed1( ):
    def Breed1(self):
        print("Dog breed 1 is German shepard")
class Dog_Breed2(Dog_Breed1):
    def Breed2(self):
        print("Dog breed 2 is Bulldog")
class Dog_Breed3(Dog_Breed2):
    def Breed3(self):
        print("Dog breed 3 is poodle")
a=Dog_Breed3( )
a.Breed1( )
a.Breed2( )
a.Breed3( )'''

#super( )
#The super function is used to give access to methods and properties of a parent or a sibling class
#The super function returns an object that represents the parent class
#In python super function is used to call methods from a parent(super class) inside a child(sub class) it allows to extend or override
#inherited methods while still reusing the parent functionalty

'''class parent( ):
    def __init__(self,name):
        self.name=name
        print("parent class constructor")
class child(parent):
    def __init__(self,name,age):
        super( ).__init__(name)
        self.age=age
        print("child class constructor")
c=child(input("Enter name: "),int(input("Enter age: ")))
print(c.name)
print(c.age)'''
