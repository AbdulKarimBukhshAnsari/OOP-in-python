"""Static method are simple it does not depend upon any instance , we use them without self"""

class Student():
    def __init__(self,name):
        self.name = name

    @staticmethod
    def greet(name):
        return(f"hello world: {name}")


print(Student.greet("karim"))  #you don't need to create any instance to use this function 