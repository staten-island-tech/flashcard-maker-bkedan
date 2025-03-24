class student:
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes
    def work(self, homework):
        self.classes.remove(homework)
        print(self.classes)
ethan = student("Ethan", ['APWH Seminar', 'Trig Exam', 'Peterson Exam', 'Chemistry Quiz'])
ethan.work('Peterson Exam')