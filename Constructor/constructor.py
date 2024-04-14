"""Constructor is basically the initialization of your class 
you can make the constructor by using __init__ method and if you 
don't define the constructor then python will take the constructor by
itself"""

class Student:
    def __init__(self):
        print("Hello World!")
        print("Karim")

#All the things which will you do in construcor will be executed by itself.
s_1 = Student()
#Every time you make objects the constructor will be executed 
s_2 = Student()

