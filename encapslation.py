#Encapslation
#Combine multiple units into single unit is known it as a encapslation
#We have 3 steps
#Public data
#_Protective data
#__Private data

#public data
'''class parent( ):
    publicdata=10
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj1=child( )
obj1.method1( )
obj1.method2( )'''

#protected data
'''class parent( ):
    _protectivedata=10
    def method1(self):
        print(self._protectivedata)
class child(parent):
    def method2(self):
        print(self._protectivedata)
obj1=child( )
obj1.method1( )
obj1.method2( )
print(obj1._protectivedata)'''

#private data
'''class parent( ):
    __privatedata=10
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child( )
obj1.method1( )
obj1.method2( )
print(obj1._parent__privatedata)'''











