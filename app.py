import json

class student:
    def __init__(self, name, classes, assignments):
        self.name = name
        self.classes = classes
        self.assignments = assignments

    def display_info(self):
        return{"name": self.name, "classes": self.classes, "assignments": self.assignments}
student = student("Ethan", "Chemistry", "Seminar")
