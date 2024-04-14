"""There are two types of attributes mainly which are
1) Class Attributes
2) Object Attributes
"""
"""Class attributes would remain same for all instances of the class and it will be define outside
of the construcor without self"""

"""Object attrubutes would be different for you and you can change it for different objects easily"""

class Student:
    name = "Yasir"  # this is class attribute

    def __init__(self,name):
        self.name = name #this is object attribute , if we have the same name of class and object then we will give preference to object


s_1 = Student("Karim")
print(s_1.name)