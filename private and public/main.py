"""Private attribute
That attributes which can only be used within the class are called private attributes"""
"""Public Attributes:
Those attributes which can be used outside the class are called public attributes
Same things can be done with """
class Student:
    def __init__(self,name) :
        self.__name = name  #by using double undercore you can make attributes and function private
    def __hello(self): # you can also make the function private
        print("Hello ",self.__name)
s1 = Student("karim")
print(s1.__name) #you can't access the name outside the class it will through error
#you can access the private attributes inside the class
