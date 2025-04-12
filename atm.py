# Define a class for the ATM system
class ATM:
    def __init__(self):
        # Initialize a dictionary to store account information
        # Each account is associated with a PIN and a balance
        self.accounts = {
            "12345": {"pin": "1234", "balance": 1000},
            "67890": {"pin": "5678", "balance": 500},
        }

    # Method to authenticate user based on account number and PIN
    def authenticate(self, account_number, pin):
        # Check if the account number exists and the PIN matches
        if account_number in self.accounts and self.accounts[account_number]["pin"] == pin:
            return True  # Authentication successful
        return False  # Authentication failed

    # Method to check the balance of an account
    def check_balance(self, account_number):
        # Return the current balance of the account
        return self.accounts[account_number]["balance"]

    # Method to withdraw money from an account
    def withdraw(self, account_number, amount):
        # Check if the withdrawal amount exceeds the available balance
        if amount > self.accounts[account_number]["balance"]:
            print("Insufficient balance.")
        else:
            # Deduct the withdrawal amount from the account balance
            self.accounts[account_number]["balance"] -= amount
            print(f"Withdrawal successful. Remaining balance: {self.accounts[account_number]['balance']}")

    # Method to deposit money into an account
    def deposit(self, account_number, amount):
        # Add the deposit amount to the account balance
        self.accounts[account_number]["balance"] += amount
        print(f"Deposit successful. New balance: {self.accounts[account_number]['balance']}")

    # Method to change the PIN of an account
    def change_pin(self, account_number, old_pin, new_pin):
        # Check if the old PIN is correct
        if self.accounts[account_number]["pin"] == old_pin:
            # Update the PIN if the old PIN is correct
            self.accounts[account_number]["pin"] = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN.")

# Main function to run the ATM simulator
def main():
    # Create an instance of the ATM class
    atm = ATM()
    print("Welcome to the ATM Simulator!")

    # Main loop to handle user interactions
    while True:
        # Display the main menu options
        print("\n1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        # Handle login option
        if choice == "1":
            # Prompt user to enter account number and PIN
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")

            # Authenticate the user
            if atm.authenticate(account_number, pin):
                print("\nLogin successful!")
                # Inner loop to handle post-login operations
                while True:
                    # Display post-login menu options
                    print("\n1. Check Balance")
                    print("2. Withdraw")
                    print("3. Deposit")
                    print("4. Change PIN")
                    print("5. Logout")
                    choice = input("Enter your choice: ")

                    # Handle balance check option
                    if choice == "1":
                        # Display the current balance
                        print(f"Your balance is: {atm.check_balance(account_number)}")
                    # Handle withdrawal option
                    elif choice == "2":
                        # Prompt user to enter withdrawal amount
                        amount = float(input("Enter the amount to withdraw: "))
                        # Perform withdrawal
                        atm.withdraw(account_number, amount)
                    # Handle deposit option
                    elif choice == "3":
                        # Prompt user to enter deposit amount
                        amount = float(input("Enter the amount to deposit: "))
                        # Perform deposit
                        atm.deposit(account_number, amount)
                    # Handle PIN change option
                    elif choice == "4":
                        # Prompt user to enter old and new PINs
                        old_pin = input("Enter your old PIN: ")
                        new_pin = input("Enter your new PIN: ")
                        # Change the PIN
                        atm.change_pin(account_number, old_pin, new_pin)
                    # Handle logout option
                    elif choice == "5":
                        print("You have logged out.")
                        break  # Exit post-login loop
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid account number or PIN.")
        # Handle exit option
        elif choice == "2":
            print("Thank you for using the ATM Simulator!")
            # Exit the program
            exit()
        else:
            print("Invalid choice. Please try again.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
