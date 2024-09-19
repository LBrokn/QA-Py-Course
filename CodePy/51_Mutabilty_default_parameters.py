from typing import List, Optional

#class Student:
    #def __init__(self, name: str, grades: List[int] = []): #"This is bad!" Never make a parameter equal to a mutable valuable by default
      #  self.name = name
      #  self.grades = grades

   # def take_exam(self, result:int):
        #self.grades.append(result)

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result:int):
        self.grades.append(result)

bob = Student("Bob")
name2 = Student("Name2")
bob.take_exam(90)
print(bob.grades)
print(name2.grades)
        