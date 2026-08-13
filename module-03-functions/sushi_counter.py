"""
🍣 Sushi Roll Counter - Functions Practice
Turning the inventory logic from module-01 and module-02
into reusable functions.
"""


def calculate_revenue(rolls_sold, price_per_roll):
    """Total money made from rolls sold today."""
    return rolls_sold * price_per_roll


def calculate_remaining_stock(rolls_in_stock, rolls_sold):
    """Rolls left after today's sales."""
    return rolls_in_stock - rolls_sold


def classify_stock_level(remaining_stock):
    """Describe how urgently the shop needs to restock."""
    if remaining_stock >= 30:
        return "well stocked ✅"
    elif remaining_stock >= 15:
        return "getting low ⚠️"
    elif remaining_stock >= 1:
        return "restock now! 🔴"
    else:
        return "SOLD OUT 🚨"


def needs_restock(remaining_stock, threshold=15):
    """True if stock has dropped to or below the restock threshold."""
    return remaining_stock <= threshold


def print_inventory_report(roll_name, rolls_in_stock, rolls_sold, price_per_roll):
    """Print a full inventory report for one roll type, using the functions above."""
    revenue = calculate_revenue(rolls_sold, price_per_roll)
    remaining = calculate_remaining_stock(rolls_in_stock, rolls_sold)
    stock_status = classify_stock_level(remaining)
    restock_flag = needs_restock(remaining)

    print("=" * 40)
    print(f"🍣 {roll_name.upper()} — DAILY INVENTORY")
    print("=" * 40)
    print(f"Starting stock: {rolls_in_stock}")
    print(f"Rolls sold today: {rolls_sold}")
    print(f"Remaining stock: {remaining}")
    print(f"Revenue: ${revenue:.2f}")
    print(f"Status: {stock_status}")
    if restock_flag:
        print("📋 Action: Add to restock order!")
    print("=" * 40)


# --- Use the functions ---
print_inventory_report(
    roll_name="Rainbow Roll",
    rolls_in_stock=40,
    rolls_sold=28,
    price_per_roll=12.49,
)

print()

print_inventory_report(
    roll_name="California Roll",
    rolls_in_stock=20,
    rolls_sold=19,
    price_per_roll=7.99,
)