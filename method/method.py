"""Methods are the special type of functions that belong to the special class we can simply call them with object.function_name()"""


class Student():
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hello {self.name}")


s_1 = Student("karim")
s_1.greet()
