import json

class teach:
    def __init__(self):
        self.aa = {}

    def makekey(self):
        key = input("Give key: ")
        value = input("Give value: ")
        self.aa[key] = value
        print(self.aa)

    def save(self):
        with open("FlashCards.json", 'w') as file:
            json.dump(self.aa, file, indent=4)

w = teach()
w.makekey()
w.save()

class student:
    def __init__(self, point, streak):
        self.point = point
        self.streak = streak
        point = 0
        streak = 0 
    
    def display_info(self):
        return f"student: {self.bonus}, streak: {self.streak}"
    
    def to_dict(self):
        return {"bonus": self.bonus, "streak": self.streak}
   


