import json

class Student:
    def __init__(self, name, classes, homework):
        self.name = name
        self.classes = classes
        self.homework = homework
    def display_info(self):
        return f"{self.name} {self.classes} {self.homework}"

    def to_dict(self):
        return {"name": self.name, "classes": self.classes, "homework": self.homework}
students_data = [Student.to_dict() for x in Student]
print(students_data)