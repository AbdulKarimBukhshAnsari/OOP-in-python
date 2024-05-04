"""As every object and its attributes will take place in memory so we simply del the object when we have used it 
for that purpose we simply use del keyword"""
class Student:
    def __init__(self,name) :
        self.name = name



s1 = Student("karim")
print(s1.name)
del s1
print(s1.name)