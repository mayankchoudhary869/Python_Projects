def tip_splitter():
    print("=== Tip Splitter ===")
    try:
        total_bill = float(input("Enter total bill amount: ₹"))
        tip_percent = float(input("Enter tip percentage (e.g., 15 for 15%): "))
        num_people = int(input("Enter number of people splitting the bill: "))

        if total_bill < 0 or tip_percent < 0 or num_people <= 0:
            print("❌ Please enter positive values for all inputs.")
            return

        tip_amount = (tip_percent / 100) * total_bill
        total_amount = total_bill + tip_amount
        amount_per_person = total_amount / num_people

        print(f"\n💡 Tip amount: ₹{tip_amount:.2f}")
        print(f"💡 Total amount (with tip): ₹{total_amount:.2f}")
        print(f"💡 Each person pays: ₹{amount_per_person:.2f}")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    tip_splitter()
