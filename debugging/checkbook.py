class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Deposit must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        self.get_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Withdrawal must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            self.get_balance()

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    cb = Checkbook()
    while True:
        print("\nAvailable actions: deposit, withdraw, balance, exit")
        action = input("What would you like to do? ").lower().strip()
        if action == 'exit':
            print("Thank you for using the Checkbook. Goodbye!")
            break
        elif action in ['deposit', 'withdraw']:
            try:
                amount = float(input(f"Enter the amount to {action}: $"))
                if action == 'deposit':
                    cb.deposit(amount)
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
