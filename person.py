class Person:

    def __init__(self,user_name,user_country):
        self.user_name = user_name
        self.user_country = user_country


    def __str__(self):
        return '{},{}'.format(self.user_name,self.user_country)


    def greet(self):
        if self.user_country == 'pakistan':
            return "Assalam o Alaikum"

        else:
            return "Hello"


p1 = Person('Muqadsa','pakistan')
print(p1)
print(p1.user_country)
p1.gender = 'female'
print(p1.gender)
p2 = p1
print(p1.user_name)
print(p2.user_name)
p2.user_name = 'Ali'
print(p1.user_name)
print(p2.user_name)
