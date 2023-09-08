class Fraction:

    def __init__(self,p,q):
        self.num = p
        self.den = q

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

    def __add__(self,other):
        num = self.num*other.den + self.den*other.num
        den = self.den*other.den
        return '{}/{}'.format(num,den)

    def __sub__(self,other):
        num = self.num*other.den-self.den*other.num
        den = self.den*other.den
        return '{}/{}'.format(num,den)

    def __mul__(self,other):
        num = self.num*other.num
        den = self.den*other.den
        return '{}/{}'.format(num,den)

    def __truediv__(self,other):
        num = self.num*other.den
        den = self.den*other.num
        return '{}/{}'.format(num,den)
    
    def convert_to_decimal(self):
        return self.num/self.den
        
        

obj1 = Fraction(3,4)
print(obj1)
obj2 = Fraction(1,2)
print(obj2)
print(obj1 + obj2)
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 / obj2)
print(obj1.convert_to_decimal())
