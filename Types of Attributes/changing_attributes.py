"""If we want to change the attributes of the object and classes we can do so"""
#changing object attributes
class Student():
    def __init__(self,name):
        self.name = name


student = Student("karim")
print(student.name) 
student.name = "haseeb" #this is how can we change the object attributes
print(student.name) #the name would be changed