import datetime

def print_receipt(items, tax_rate=0.05):
    print("\n===== 🧾 RECEIPT =====")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("----------------------------")
    subtotal = 0
    for item in items:
        name = item['name']
        qty = item['quantity']
        price = item['price']
        total = qty * price
        subtotal += total
        print(f"{name} x{qty} @ ₹{price:.2f} = ₹{total:.2f}")
    print("----------------------------")
    tax = subtotal * tax_rate
    grand_total = subtotal + tax
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Tax (5%): ₹{tax:.2f}")
    print(f"Total:    ₹{grand_total:.2f}")
    print("============================\n")

def main():
    print("=== 🛒 Mini POS Billing System ===")
    items = []

    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item (₹): "))
            items.append({"name": name, "quantity": quantity, "price": price})
        except ValueError:
            print("❌ Invalid input. Please enter numeric values for quantity and price.\n")

    if items:
        print_receipt(items)
    else:
        print("🛑 No items entered. Exiting.")

if __name__ == "__main__":
    main()