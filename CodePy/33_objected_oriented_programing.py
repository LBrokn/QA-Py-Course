#student = {"name": "Rolf", "grades":(89, 90, 93, 78, 90)}

#def average(sequence):
  #  return sum(sequence)/ len(sequence)

#print(agerage(student["grades"]))

#class Student:
    #def __init__(method):
        

  #  def average(method):
   #     return sum(method.grades)

#student = Student()
#print(student.name)
#print(student.grades)
#average(student.grades)


#methods. functions inside a class is a method
#def average(self):
        #return sum(self.grades) / len(self.grades)
        #name to acess the name paramater
#print(Student.average(student))

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades #(90, 90, 93, 78, 90)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Name2", (90, 90, 93, 78, 90))

print(student.average_grade())
print(Student.average_grade(student2))


