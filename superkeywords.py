"""class Phone:
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
        #syntax to call parent ka buy method
        super().buy()

        
s = Smartphone(20000,"apple",13)
s.buy()
"""
class Phone:

    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class Smartphone(Phone):

    def __init__(self,price,brand,camera,os,ram):
        print("inside smartphone constructor")
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram
        print("inside smartphone constructor")

s = Smartphone(20000,"sumsung",13,"aandorid",2)
# is example my phly control obviuosly vchild constrctor k pass gya first line print
#hoi phir us k bas uper keyword usy parent k pass ly gya wahn first line print hoi or
#variable ya members initializa huy or dobara child k pass aya baqi k variable initializa
#hoy or phir akhri lline execute hoi thats the power of super keyword
#super hamesha class k andar use ho ga
#you cant access attributes using super only methods can access using super
