class Father:
    money = 10000

    def show(self):
        print('parent class instance method')

    @classmethod
    def show_money(cls):
        print('parent class class method',cls.money)


    @staticmethod
    def stat():
        a = 10
        print('parent class static method:',a)

class Son(Father):
    def disp(self):
        print('child class instance method')

s = Son()
s.disp()     #accessing son class members by using son class object
s.show()      # accessing father class members by using son class object
s.show_money()
s.stat()
print()
f = Father()
f.show()
f.show_money()
f.stat()
# we cant use father object to access child class members