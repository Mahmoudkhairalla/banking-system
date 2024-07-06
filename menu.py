class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} successfully.")
        else:
            print("Deposit amount must be greater than zero.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} successfully.")
        else:
            if amount > self.balance:
                print("Insufficient balance.")
            else:
                print("Withdrawal amount must be greater than zero.")
    
    def check_balance(self):
        print(f"Current balance for {self.name}: ${self.balance}")

def main():
    accounts = {}

    while True:
        print("\n===== Banking System Menu =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter account holder's name: ")
            if name in accounts:
                print("Account already exists.")
            else:
                accounts[name] = Account(name)
                print(f"Account created successfully for {name}.")
        
        elif choice == '2':
            name = input("Enter account holder's name: ")
            if name in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[name].deposit(amount)
            else:
                print("Account not found.")
        
        elif choice == '3':
            name = input("Enter account holder's name: ")
            if name in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[name].withdraw(amount)
            else:
                print("Account not found.")
        
        elif choice == '4':
            name = input("Enter account holder's name: ")
            if name in accounts:
                accounts[name].check_balance()
            else:
                print("Account not found.")
        
        elif choice == '5':
            print("Thank you for using the Banking System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
