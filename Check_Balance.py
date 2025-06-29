def show_menu():
    print("\n=== Bank Account Menu ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def main():
    balance = 0.0
    print("Welcome to the Simple Bank Account!")
    
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print(f"💰 Your current balance is: ₹{balance:.2f}")

        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount > 0:
                    balance += amount
                    print(f"✅ Deposited ₹{amount:.2f}. New balance: ₹{balance:.2f}")
                else:
                    print("❌ Please enter a positive amount.")
            except ValueError:
                print("❌ Invalid input. Please enter a numeric amount.")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"✅ Withdrawn ₹{amount:.2f}. New balance: ₹{balance:.2f}")
                    else:
                        print("❌ Insufficient balance.")
                else:
                    print("❌ Please enter a positive amount.")
            except ValueError:
                print("❌ Invalid input. Please enter a numeric amount.")

        elif choice == '4':
            print("Thank you for using Simple Bank Account. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
