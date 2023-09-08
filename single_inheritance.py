#SINGLE INHERITANCE
class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")

class Smartphone(Phone):
    pass

Smartphone(1000,"apple",13).buy()

#MULYILEVEL
