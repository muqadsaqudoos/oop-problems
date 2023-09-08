class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

#bahar function banaya
def greet(person):
    print('HI my name is ',person.name,'i am a ',person.gender)
    p = Person('Muqadsa','female')
    return p
#yahan sy class ka objject banaya
p = Person('Muqadsa','female')
#phir is ko bahar waly function my call kar dia
x = greet(p)
print(x.name)
print(x.gender)
#bahar function k andar aik object ban ka bahar a k bhi call kar
#sakty ha basically asa bhi ho sakta ha"""
#technically object ka adress bhej ha rahy ha andar object kko nahi bhejj rhay ha
# or aesa ho sakta ha agar ink kki ip nikaly gy to same ho gi
