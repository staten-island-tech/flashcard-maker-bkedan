streak = 0
import json

class teach:
    def __init__(self):
        self.aa = {}

    def makekey(self):
        key = input("Give key: ")
        value = input("Give value: ")
        self.aa[key] = value
        print(self.aa)
    def show(self):
        print(self.ok)
    def save(self):
        with open("FlashCards.json", 'w') as file:
            json.dump(self.aa, file, indent=4)

w = teach()
w.makekey()
w.save()

class student:
    def __init__(self, teach_instance):
        global streak
        self.teach_instance = teach_instance
    def start():
        global streak
        for key, value in self.teach_instance:
            print(key)
            x = input("give value")
            if x == value:
                streak += 1
                print(streak)
            else: 
                print("no")
student()
   


