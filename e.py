import json
streak = 0

class teach:
    def __init__(self):
        self.aa = {}

    def makekey(self):
        key = input("Give key: ")
        value = input("Give value: ")
        self.aa[key] = value
        print(self.aa)

    def show(self):
        print(self.aa)

    def save(self):
        with open("FlashCards.json", 'w') as file:
            json.dump(self.aa, file, indent=4)

class student:
    def __init__(self, teach_instance):
        global streak
        self.teach_instance = teach_instance

    def start(self):
        global streak
        for key, value in self.teach_instance.aa.items():
            print(key)
            x = input("Give value: ")
            if x == value:
                streak += 1
                print(f"Correct! Streak: {streak}")
            else:
                print("Incorrect, you a loser")

w = teach()
w.makekey()
w.save()

s = student(w)
s.start()
