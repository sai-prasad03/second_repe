class Father:
    def __init__(self,m,j):
        self.money = m
        print('constructor of father class ')

    def show(self):
        print('instace method of father class')

class Son(Father):
    def __init__(self,m,j):
        super().__init__(m,j)     #calling parent class constructor
        self.job = j
        print('constructor of  child class')

    def disp(self):
        print('instance method of child class',self.money,self.job)


s = Son(1000,'python')
s.disp()