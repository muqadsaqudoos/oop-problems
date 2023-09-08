"""#METHOD OVERRIDING
class Phone:
    def buy(self):
        print('Phone')

class Smartphone(Phone):
    def buy(self):
        print('SmartPhone')
s = Smartphone()
s.buy()
#if child and parent have same name method it will call itself
"""

#Method Overlaoding
"""class Shape:
    def area(self,radius):
        return 3.14*radius**2
    def area(self,l,b):
        return l*b

s = Shape()
s.area(2)
s.area(3,4)"""
#it will give error bcz pythin does not allow this 
#it is use for readability

#for this you can use if else
"""class Shape:
    def area(self,a,b=0):
        if b==0:
            return 3.14*a**2
        else:
            return a*b

s = Shape()
print(s.area(2))
print(s.area(3,4))"""

#Opertor Overloading

print("hello"+"world")#canactenation
print(3+4)#Addition
print([1,2,3]+[4,5,6])#merging
