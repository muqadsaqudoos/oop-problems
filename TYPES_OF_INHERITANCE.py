#SINGLE INHERITANCE
"""class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")

class Smartphone(Phone):
    pass

Smartphone(1000,"apple",13).buy()"""

#MULYILEVEL
"""class Product:
    def review(self):
        print("product coutomer review")

class Phone(Product):
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")
        
class Smartphone(Phone):
    pass

s=Smartphone(1000,"apple",13)
s.buy()# we can access the parent and grandparent methods
s.review()"""
#HRARICAL

"""class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")

class Smartphone(Phone):
    pass
class Featurephone(Phone):
    pass
Smartphone(1000,"apple",13).buy()
Featurephone(100,"nokia",13).buy()"""
#MULTIPLE
"""class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")
class Product:
    def review(self):
        print("product coutomer review")

class Smartphone(Phone,Product):
    pass
s=Smartphone(1000,"apple",13)
s.buy()
s.review()"""
#HYBRID
class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")
class Product:
    def buy(self):
        print("buying a phone BY PRODUCT METHOD")
#METHOD RESOLUTION ORDER(MRO)
class Smartphone(Product,Phone):#YAHAN PAR JIS KA NAME PHLA LIKHA HO GA US KA METHOD EXECUTE HO GA
    pass
s=Smartphone(1000,"apple",13)
s.buy()
