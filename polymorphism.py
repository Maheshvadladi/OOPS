#Polymorphism
#operator overloading
'''a=2 ; b=4
print(a+b)
print(a.__add__(b))
print(a.__sub__(1))
print(a.__mul__(2))
#print(a.__div__(2)) Error
print(a.__pow__(2))
print(a.__le__(8))
print(a.__ge__(3))'''

'''a=[1,2,3,4,5,6,7] ; b=[6,7,8,9,10,11,12]
print(a.__add__(b))
print(a.__getitem__(2))
print(b.__getitem__(3))'''

'''a="code" ; b="gnan"
print(a.__add__(b))
a="python" ; b="course"
print(a.__add__(b))
print("mahesh".__add__(" "+"vadladi").title())'''

#operator overriding
'''class A( ):
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B( ):
    def __init__(self,b):
        self.b=b
x=A(6)
y=B(4)
print(x+y)'''

#method overloading
'''class New( ):
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is:",a+b+c)
        elif a!=None and b!=None:
            print("the product is:",a*b)
        else:
            print("program ends")
x=New( )
x.sum( )
x.sum(3,4,5)
x.sum(6,2)'''

#method overriding
'''class Animal( ):
    def speak(self):
        print("animal can make sounds")
class Dog( ):
    def speak(self):
        print("Dog can bark")
a=Animal( )
b=Dog( )
a.speak( )
b.speak( )'''
