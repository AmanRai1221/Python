import time # Import the time module
class ATM:
    def __init__(self):
        # Initialize the ATM with a default balance and PIN
        self.balance = 0  # Account balance starts at $0.00
        self.pin = 1234   # Default PIN for the ATM
        self.transaction_history = []  # List to store transaction history
        self.authorize = False

    def welcome(self):
        print("\n=================================") 
        print("\n==== Welcome to Bank of India ===") # Display a welcome message
        print("\n=================================") 
        time.sleep(2)
        card = input("Please insert your card ") # Prompt user to insert their card
        upin = int(input("Enter your pin :- ")) # Prompt user to enter their PIN
        if upin == self.pin: # Check if the entered PIN matches the stored PIN
            self.authorize = True   # Set authorization to True if the PIN is correct
            print("PIN accepted.") # Inform the user that the PIN is accepted
        else:
            for attempt in range(3):  # Allow up to 3 attempts
                print("Invalid PIN. Please try again.")
                upin = int(input("Enter your pin"))
                if upin == self.pin:
                    self.authorize = True
                    print("PIN accepted.")
                print("Too many attempts ")
                print("Thank you for using the ATM. Goodbye!")  # Exit message
                break  # Exit the loop and end the program

    def display_menu(self):
        # Display the main menu options for the ATM
        time.sleep(2)
        print("\n=================================") 
        print("\n======== Bank of India ==========")
        print("\n============= Menu ==============")
        print("\n=================================") 

        print("1. Account Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

    def account_balance_inquiry(self):
        # Display the current account balance
        time.sleep(2)
        print("\n=================================") 
        print("\n======== Bank of India ==========")
        print("\n======= Balance Inquiry =========")
        print("\n=================================")

        print(f"Your current balance is: {self.balance}")

    def cash_withdrawal(self):
        # Handle cash withdrawal from the account
        time.sleep(2)
        print("\n=================================") 
        print("\n======== Bank of India ==========")
        print("\n======= Cash Withdrawal =========")
        print("\n=================================")

        amount = int(input("Enter amount to withdraw: "))
        if amount > self.balance:
            # Check if there are sufficient funds
            print("Insufficient funds.")
            print(f"Your current balance is: {self.balance}")

        else:
            # Deduct the amount from the balance and record the transaction
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"Please take your cash: {amount}")
            print(f"Your current balance is: {self.balance}")


    def cash_deposit(self):
        # Handle cash deposit into the account
        time.sleep(2)
        print("\n=================================") 
        print("\n======== Bank of India ==========")
        print("\n========= Cash Deposit ==========")
        print("\n=================================")

        amount = int(input("Enter amount to deposit"))
        # Add the amount to the balance and record the transaction
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"Successfully deposited: {amount}")
        print(f"Your current balance is: {self.balance}")


    def change_pin(self):
        # Allow the user to change their PIN
        time.sleep(2)
        print("\n=================================")
        print("\n======== Bank of India ==========")
        print("\n========= Change PIN ============")
        print("\n=================================")

        upin = int(input("Enter your old PIN: "))

        if upin == self.pin:
            # Check if the entered PIN matches the stored PIN
            new_pin = int(input("Enter new PIN: "))
            self.pin = new_pin  # Update the PIN
            print("PIN changed successfully.")
            print(f"Your new PIN is: {self.pin}")
        else:
            for attempt in range(3):  # Allow up to 3 attempts
                print("Invalid PIN. Please try again.")
                upin = int(input("Enter your old pin"))
                if upin == self.pin:
                    new_pin = int(input("Enter new PIN: "))
                    self.pin = new_pin  # Update the PIN
                    print("PIN changed successfully.")
                    print(f"Your new PIN is: {self.pin}")
                print("Too many attempts ")
                break
    def transaction_history_display(self):
        # Display the transaction history
        time.sleep(2)
        print("\n=================================")
        print("\n======== Bank of India ==========")
        print("\n====== Transaction History ======")
        print("\n=================================")

        print("\n--- Transaction History ---")
        if not self.transaction_history:
            # Check if there are no transactions
            print("No transactions found.")
        else:
            # Print each transaction in the history
            for transaction in self.transaction_history:
                print(transaction)

    def run(self):
        # Main loop to run the ATM simulation
        self.welcome()
        while (self.authorize==True):
            self.display_menu()  # Show the menu options
            choice = input("Select an option (1-6): ")  # Get user choice
            if choice == '1':
                self.account_balance_inquiry()  # Option 1: Check balance
            elif choice == '2':
                self.cash_withdrawal()  # Option 2: Withdraw cash
            elif choice == '3':
                self.cash_deposit()  # Option 3: Deposit cash
            elif choice == '4':
                self.change_pin()  # Option 4: Change PIN
            elif choice == '5':
                self.transaction_history_display()  # Option 5: View history
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")  # Exit message
                break  # Exit the loop and end the program
            else:
                print("Invalid option. Please try again.")  # Handle invalid input

atm = ATM()  # Create an instance of the ATM class
atm.run()  # Start the ATM simulation