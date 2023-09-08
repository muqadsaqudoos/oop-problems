class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")

class Smartphone(Phone):
    def buy(self):
        print("buying a smartphone")
#if child and parent have same method then on calling parent method will called
s = Smartphone(20000,"apple",13)
s.buy()
