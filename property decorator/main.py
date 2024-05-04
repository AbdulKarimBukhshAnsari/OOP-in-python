"""When we want to define the method as a property we use property decorator
Example:
Suppose you wanna find the percenatge of any student and you simply took the number of that student 
after that you realized that the student marks is lesser than you entered if you have calulated the percenatge 
by current values and you tried to change the percenatge as well you can't because it will give the resulyt
of previous data , but if you have defined these attribute in the property decorator you can do so .This 
function will return the latest value itself and will give the result of last option.
The most important thing in property decorator ,it will write the latest value and the chaneg will appear in it."""

class Student:
    def __init__(self,phy,che,math):
        self.phy= phy
        self.chem = che
        self.math = math
        self.percent = ((self.phy+self.chem+self.math)/300) *100
    @property
    def change(self):
        self.percentage = ((self.phy+self.chem+self.math)/300) *100
        return self.percentage

#suppose you made the object of student class which is S:
s = Student(98,100,99)
print(s.percent)
s.phy = 89
print(s.percent) #the change will not appear in it
print(s.change)    #the change will appear in this option ,because we use property decorator

    