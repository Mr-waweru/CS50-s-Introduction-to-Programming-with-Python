#####################################################################

"""
class My_class():
    def __init__(self, parameter1, parameter2) -> None:
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    def __str__(self) -> str:
        speed = self.parameter1 + self.parameter2
        return f"The speed is: {speed}km/h"

    def drive(self):
        return self.parameter1 + self.parameter2


car = My_class(50, 60)
print(car)
"""
#####################################################################
"""
class App():
    def __init__(self, users, storage, username) -> None:
        self.users = users
        self.storage = storage
        self.username = username

    def __str__(self) -> str:
        return f"App Details: Username: {self.username}, User: {self.users}, Storage: {self.storage}"

    def loging(self):
        if self.username == "owner" and self.users >= 1:
            return (
                f"Welcome, {self.username}.\n" 
                f"Your storage is: {self.storage}."
            )
        else:
            return "Login is denied!"
        
    def increase_capacity(self, number):
        self.storage += number
        return f"Updated storage: {self.storage}."
    

product_one = App(35, 256, "owner")
print(product_one)
print(product_one.loging())
print(product_one.increase_capacity(50))
print()

product_two = App(35, 128, "josh")
print(product_two)
print(product_two.loging())
"""
#####################################################################

class OnLineCourse:
    def __init__(self, course, instructor) -> None:
        self.course = course
        self.instructor = instructor
        self.students = []

    def __str__(self) -> str:
        return f"Course Details."

    def enroll_students(self, name):
        self.students.append(name)
        return f"{name} has been enrolled in the {self.course} course."

    def course_details(self):
        return (
            f"Course: {self.course}\n"
            f"Instructor Name: {self.instructor}\n"
            f"Enrolled Students: {','.join(self.students)}"
        )
    
    def completed_course(self, name):
        if name in self.students:
            self.students.remove(name)
            return f"{name} has completed the course"
        else:
            return f"{name} is not enrolled in this course"
        
    def avrg_grade(self, grades):
        total = sum(grades)
        average = total / len(grades)
        return f"The average grade is: {average}"
    

course_input = input("Enter a course: ").lower().strip()
name = input("Enter Instructor: ").title().strip()
student = input("Enter a name: ").lower().strip()

course = OnLineCourse(course_input, name)
grades = [65, 70, 75, 80, 85]

print(course)
print(course.enroll_students(student))
print(course.course_details())
print(course.avrg_grade(grades))
# print(course.completed_course(name="bob"))
