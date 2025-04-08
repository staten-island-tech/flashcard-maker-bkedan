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
        try:
            with open("FlashCards.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []  

        data.append(self.aa)

        with open("FlashCards.json", "w") as file:
            json.dump(data, file, indent=4)

w = teach()
w.makekey()
w.save()
