class Army:
    def __init__(self):
        self.name = 'rahul'
        self.gn = 'Gun()'

    def show(self):
        print('Name:',self.name)

class Gun:
    def __init__(self):
        self.name = 'AK47'
        self.capacity = '75 Rounds'
        self.Lenght = '34.3 In'

    def disp(self):
        print('Name:',self.name)
        print('capacity:',self.capacity)
        print('Lenght:',self.Lenght)

a = Army()
a.show()
print()

a.gn = Gun()
a.gn.disp()
print()

g = a.gn
g.disp()
print(a.gn.name)
print(g.capacity)

