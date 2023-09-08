#constructor example if child consrtuctor is not present then pareent constructor will call
"""class Phone:

    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")


class Smartphone(Phone):
    pass

s=Smartphone(20000,"apple",13)
"""



#constructor examplel 2 when child has a constructor then those parent consrtuctor will not execute

"""class Phone:

    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class Smartphone(Phone):

    def __init__(self,os,ram):
        self.os = os
        self.ram = ram
        print("inside smartphone constructor")

s = Smartphone("aandorid",2)
"""

#child cant access private members of the parennt class

class Phone:

    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def show(self):
        print(self.__price)

class Smartphone(Phone):
    def check(self):
        print(self.__price)


s = Smartphone(20000,"apple",13)#is my error ay ga bcz yr private member ha
s.check()
