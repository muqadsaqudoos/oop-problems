class User:#PARENT CLASS
    def __init__(self):
        self.name = 'nitish'

    def login(self):
        print('login')

class Student(User):#CHILD CLASS          # is jaga my student ka constructor use nahi kery                           #
                                           # is ki reason ye ha k jab hum s object ko call karty ha to wo apni class my ja k constructor ko find karta ha if it does'nt
    def enroll(self):                       # find a constructor then it will go to the parent class and will fetch name if the consturctuor is present in the child
        print('enroll into the course')   #tclass then it will not go to the parent class we will never br able to fetch the name so remember this rule muqadsa

u = User()
s = Student()
print(s.name)
s.login()
s.enroll()
