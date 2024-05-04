"""
Class Method:
A class method is bound to the class and recieves the class as an implicit and as an argument.
Note : The static method can't access or update the values of the class
"""


#Example for changing the attributes of class method

class Student:
    class_student = "Five"
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
    def changing(self,new_class):
        Student.class_student = new_class # by using this method we can modify the value of class
        #self.__class__.class_student = new_class --> by using this method we can also do the same thing 
        
s = Student("Yasir",23045)
print(s.class_student)
s.changing("Six")
print(s.class_student)
