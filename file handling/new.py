class Mobil:
    def __init__(self,m,v):
        self.model = m
        self.volume = v

    def show_model(self,p):
        self.price = p
        print('model',self.model,'and price',self.price)
        print('volume',self.volume)

realme = Mobil('realme X',50)
realme.show_model(15000)
