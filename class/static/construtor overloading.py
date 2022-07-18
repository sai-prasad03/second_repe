class Father:
    def __init__(self):
        self.money = 1000
        print('this is constrructor of father class')

    def show(self):
            print('instance method of father class')

class Son(Father):
    def __init__(self):
        self.money = 5000
        self.car = "Audi"
        print('this is constructor of child class')

    def disp(self):
        print('instance method of child class')


s = Son()
print(s.money)
print(s.car)
s.disp()
s.show()

