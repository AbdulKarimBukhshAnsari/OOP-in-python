"""Super method is used when we want to access anything from parent class"""
class Person:
    def __init__(self,name):
        self.name = name
class Doctor(Person):
    def __init__(self, salary,name):
        super().__init__(name) #this is how can we inherit  the value of the parent constructor 
        self.salary = salary
 
s1 = Doctor(15000,"yasir")
print(s1.name)  #accessing the value of parent class
print(s1.salary)
