class Father:
    def __init__(self,m):
        self.money = m
        print('this is constrructor of father class')

    def show(self):
            print('instance method of father class')

class Son(Father):
    def __init__(self,r):
        self.money = r
        self.car = "Audi"
        print('this is constructor of child class')

    def disp(self):
        print('instance method of child class')


s = Son(5000)
print(s.car)
s.disp()
s.show()
