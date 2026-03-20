#Create a class Account with private attribute balance. Use methods to access and update it.


class Account():
    __balance = 0

    def get_balance(self):
        print(f"The balance is : {self.__balance}")
    
    def update_balance(self,amount):
        self.__balance += amount
        print(f"New balance is : {self.__balance}")

newaccount = Account()
newaccount.get_balance()

amount = int(input("Enter amount to be added : "))

newaccount.update_balance(amount)
