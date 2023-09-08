from abc import ABC,abstractmethod
class Bankapp(ABC):

    def database(self):
        print("connected to database")

    @abstractmethod#abstaction kliye class ko abc sy import kary gy or aik
                         #abstarct method hona zarori ha
    def security(self):
        pass# we dont write code here
    #ab agar aik or abstarct method ban dy to child ko bhi wohi banana pary ha
    #otherwise error dy ga
    #ABSTACT CLASS: jis my aik abstrct method zaror ho
class Mobileapp(Bankapp):
    def mobile_login(self):
        print("login into mobile")
     # now if you dont use abstract security method here then this code will give error


    def security(self):
        print("mobile security")

s = Mobileapp()
s.database()
"""
you cant make the object of abstract class
obj = Bankapp()
this code will give error"""
