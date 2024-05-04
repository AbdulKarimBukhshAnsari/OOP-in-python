class Person:
    name = "Karim"

class Doctor(Person):
    def __init__(self,salary):
        self.salary =  salary

d = Doctor("150000")
print(d.name)
print(d.salary)
