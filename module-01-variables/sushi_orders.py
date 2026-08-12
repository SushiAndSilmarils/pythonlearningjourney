"""
🍣 Sushi Orders - Variables Practice
My first Python program!
"""

# String variables
customer_name = "Aragorn"
order_type = "Rainbow Roll"
special_instructions = "No wasabi & No Sauce on it"

# Numeric variables
quantity = 1
price_per_roll = 12.49
total_price = quantity * price_per_roll

# Boolean variables
is_regular_customer = True
has_allergies = False

# Print the order
print("=" * 40)
print("🍣 SUSHI ORDER RECEIPT")
print("=" * 40)
print(f"Customer: {customer_name}")
print(f"Order: {order_type}")
print(f"Quantity: {quantity}")
print(f"Price per roll: ${price_per_roll}")
print(f"Total: ${total_price:.2f}")
print(f"Regular customer: {is_regular_customer}")
print(f"Special instructions: {special_instructions}")
print("=" * 40)
print("Thank you! Please come again! 🍣")