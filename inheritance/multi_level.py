class Person:
    name = "karim"
class Doctor(Person):
    salary = 150000
class Surgeon(Doctor):
    def __init__(self,time):
        self.time = time

s = Surgeon(2)
print(s.name)
print(s.salary)
print(s.time)
