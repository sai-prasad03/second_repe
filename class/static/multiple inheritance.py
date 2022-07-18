# in multiple inheritance the execution of super() method is done by MRO method
#i.e multiple resolution order
# in this method the execution will be done from left to right


class Father:
    def __init__(self):
        super().__init__()           
        print('Father class constructor')

    def showF(self):
        print('Father class instance')


class Mother:
    def __init__(self):
        super().__init__()
        print('Mother class constructor')

    def showM(self):
        print('Mother class instance')

class Son(Father,Mother):
    def __init__(self):
        super().__init__()
        print('Son class constructor')

    def showS(self):
        print('Son class instance')

s = Son()
