# Simple Bill Calculator - with error handling

print("=== Welcome to the Simple Bill Calculator ===\n")

try:
    # Get price (convert string to float)
    price = float(input("Enter the price of one item: $"))

    # Get quantity (convert string to int)
    quantity = int(input("Enter the quantity you want: "))

    # Calculate total
    total = price * quantity

    # Friendly summary using an f-string
    print(f"\n{quantity} items at {price:.2f} each = {total:.2f}")
    print("\nThank you for using the Bill Calculator!")

except ValueError:
    print("\nOops! Please enter only numbers. Letters and symbols are not allowed.")
