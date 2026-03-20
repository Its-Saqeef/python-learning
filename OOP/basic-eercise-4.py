#Create a class BankAccount with attributes balance. Add methods deposit(amount) and withdraw(amount).

class BankAccount():
    amount = 0

    def deposit(self,amount):
        self.amount += amount
        print(f"Credited! New amount is : {self.amount}")

    def withdraw(self,amount):
        if amount > 0 and self.amount - amount >=0:
            self.amount -= amount
            print(f"{amount} debited! New amount is {self.amount}")
        else:
            print("Not enough balance")

account = BankAccount()

def main():
    while True:
        print("1. View current amount")
        print("2. Deposit ammount")
        print("3. Withdraw ammount")
        print("4. Exit")

        choice = input("Enter your choice : ")

        match choice:
            case "1":
                print(f"Current amount is : {account.amount}")
            case "2":
                new_ammount = int(input("Enter amount : "))
                account.deposit(new_ammount)
            case "3":
                new_ammount =  int(input("Enter amount : "))
                account.withdraw(new_ammount)
            case "4":
                break
            case _:
                print("Invalid Choice, Try again!")

if __name__ == "__main__":
    main()