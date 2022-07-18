class Father:
    def __init__(self):
        self.money = 10000
        print("father class constructor")

    def show(self):
        print('father class instance method')
class Son(Father):
    def disp(self):
        print('child class instance method')


s = Son()
s.disp()
print(s.money)
s.show()