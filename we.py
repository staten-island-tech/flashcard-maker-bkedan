class teach:
    def __init__(self):
        self.aa = {}
    def makekey(self):
        key = input("give key: ")
        value = input("give value: ")
        self.aa[key] = value 
        print(self.aa)
w = teach()
w.makekey()
