#we can also change the class attributes easily 

class Student():
    class_name = "five"

student = Student()
print(student.class_name)
Student.class_name = "six" #this is how can we change the class attributes
student_2 = Student()
print(student_2.class_name)