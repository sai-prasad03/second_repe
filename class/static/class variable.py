class Mobile:
    fp = "yes"

    def __init__(self):
        self.model = 'Realme x'

    def show_model(self):
        print("model",self.model)

    @classmethod
    def is_fp(cls):
        print("finger print",cls.fp)

realme = Mobile()
realme.show_model()
realme.is_fp()
print()
Mobile.fp = "No"
realme.is_fp()
