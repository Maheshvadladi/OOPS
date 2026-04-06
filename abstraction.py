#abstraction
'''The process of handling complexity by hiding unneccessary information from user is called abstraction'''
#abstract class
'''if a class contain one or more than one abstract method than the class is called abstract class'''
#abstract method
'''if the method is declared without implementation is called abstract method'''

'''class A():
    def method1(self):
        pass
obj1 = A()
obj1.method1()'''

'''from abc import ABC, abstractmethod
class A():
    @abstractmethod
    def method1(self):
        print("python")
obj1=A()
obj1.method1()'''

'''from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("python")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method2(self):
        print("method2 is implemented")
    def method3(self):
        print("method3 is implemented")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()'''
