class Father:
    def __init__(self):
        super().__init__()
        print("Father Constructor")

    def showF(self):
        print("father")

class Mother:
    def __init__(self):
        super().__init__()
        print("Mother Constructor")

    def showM(self):
        print("mother")

class Son(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Son Constructor")

    def showS(self):
        print("SON")

s=Son()
print(s)
