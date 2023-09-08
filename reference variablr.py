class Person:

    def __init__(self,user_name,user_country):
        self.user_name = user_name
        self.user_country = user_country

p1 = Person('Muqadsa','pakistan')
p2 = p1
print(p1.user_name)
print(p2.user_name)
p2.user_name = 'Ali'
print(p1.user_name)
print(p2.user_name)
#yye reference variable ka concept ha jis my aik referce variable sy object ko
#allocate karty ha or phir bad my us ko dosary variable k sath allocate
#kkar dia ha lekin doono aik hi object ko allocate kar rahy ha agar aik my bhi
#changing kary gy to dono my hi changes ho gy

