class Coustomer:

    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)

    def new_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.new_address(new_city,new_pin,new_state)
        


class Address:

    def __init__(self,city,pin,state):
        self.__city = city
        self.pin = pin
        self.state = state

    def get_city(self):
        return self.__city

    def new_address(self,new_city,new_pin,new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state

         
add1 = Address('lahore','1234','punjab')
coust1 = Coustomer('muqadsa','female',add1)
coust1.print_address()
coust1.new_profile('sana','karachi','3456','sindh')
coust1.print_address()
#ab agar hum attributes ko private kar dy tab hum is ko print nahi kar saky gy is k liye we have to use
#getter setter
#Aggregation is basically relation between two classes
