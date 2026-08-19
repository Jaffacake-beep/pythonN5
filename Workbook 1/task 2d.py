#!/usr/bin/env python3

def main():
    try:
        raw = input("Enter full price of the product: ").strip()
        cleaned = raw.replace("$", "").replace(",", "")
        price = float(cleaned)
        if price < 0:
            print("Price cannot be negative.")
            return
    except ValueError:
        print("Invalid price entered.")
        return

    discount_rate = 0.20
    saving = price * discount_rate
    final_price = price - saving

    print(f"Original price: ${price:,.2f}")
    print(f"Savings (20%): -${saving:,.2f}")
    print(f"Price after discount: ${final_price:,.2f}")

if __name__ == "__main__":
    main()
    print(" note= make sure it is in two decimal points")