class Atm:
    def __init__(self):
       self.pin = ''
       self.__balance = 0
       self.menu()

    def get_balance(self):
        return self.__balance

        
    def set_balance(self,new_value):#is jaga py ab ap check lagga sakty ho ka agar value integar ha tabhi changes allow karo
        if type(new_value) == int:  #is atarh ap koi bhi ap k variables ki value ko access nahi kary ga
        self.__balance = new_value
            
                        

    def menu(self):
        user_input = input("""HI how can i help you?
1. press 1 to create pin.
2. press 2 to change pin
3. press 3 to chack balane.
4. press 4 to withdraw.
5. Anything else to exit.
""")

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.balance_withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter your pin:")
        self.pin = user_pin

        user_balance = int(input("Enter your balance:"))
        print("\n")
        self.__balance = user_balance
        self.menu()

    def change_pin(self):
        old_pin = input("Enter old pin:")
        if old_pin == self.pin:
            new_pin = input("Enter new pin:")
            self.pin = new_pin
            print("pin updated successfully")
            print("\n")
            self.menu()

        else:
            print("old pin is wrong\n")
            self.menu()

    def check_balance(self):
        user_pin = input("Enter your pin:")
        if user_pin == self.pin:
            print("your balance is ",self.__balance)
            print("\n")
            self.menu()
        else:
            print("pin is wrong\n")
            self.menu()
            
    def balance_withdraw(self):
        user_pin = input("Enter your pin:")
        if user_pin == self.pin:
            amount = int(input("Enter amonut you want to withdraw:"))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Amount withdrawl successfully. Remaining amount is:",self.__balance)
                print("\n")
                self.menu()
            else:
                print("this amount does not exist\n")
                self.menu()
                
                
            
                

        else:
            print("pin is wrong\n")
            self.menu()
        
obj =Atm()
