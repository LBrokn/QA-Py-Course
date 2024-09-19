class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

# Create an instance of the Student class
student = Student("Bob", (90, 90, 93, 78, 90))

# Print the student's name
print(student.name)

# Print the student's average grade
print(student.average_grade())