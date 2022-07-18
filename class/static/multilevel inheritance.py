class Father:
    def __init__(self):
        print("father class constructor")

    def showf(self):
        print('father class method')

class Son(Father):
    def __init__(self):
        super().__init__()
        print("son class constructor")

    def shows(self):
        print('son class method')

class Grandson(Son):
    def __init__(self):
        super().__init__()
        print("Grandson class constructor")

    def showg(self):
        print('Grandson class method')

g = Grandson()

