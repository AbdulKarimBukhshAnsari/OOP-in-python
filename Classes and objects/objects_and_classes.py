#you can define the class like that 
"""Class is the blueprint for creating the object , Blue print defines the property which defines 
the property which you need"""
class Student:
    name = "Karim"
"""Objects are the instances of the class or we can say the members of the class"""
#you can define the object like that 
s_1 = Student()

#to use the attribute of the class 
print(s_1.name)

"""the best thing of OOP is that you can use the attributes of the class several time
depends upon how many times you have made the object """

s_2 = Student()

print(s_2.name)

