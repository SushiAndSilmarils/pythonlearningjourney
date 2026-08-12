"""
🍣 Sushi Quality Checker - Conditional Practice
"""

# Sushi order data
order_time = 5  # minutes since order placed
fish_freshness = "fresh"  # fresh, okay, old
customer_rating = 4.5  # out of 5

print("=" * 40)
print("🍣 SUSHI QUALITY CHECK")
print("=" * 40)

# Check if order is ready
if order_time < 10:
    print("⏱️ Order is fresh! Ready in under 10 minutes")
elif order_time < 20:
    print("⏱️ Order is ready!")
else:
    print("⏱️ Order took longer than expected")

# Check fish quality
if fish_freshness == "fresh":
    print("🐟 Fish is fresh! Perfect for sushi")
elif fish_freshness == "okay":
    print("🐟 Fish is okay, but could be fresher")
else:
    print("🐟 Fish is old - don't serve this!")

# Check if customer is happy
if customer_rating >= 4.5:
    print("⭐ Excellent rating! Happy customer!")
elif customer_rating >= 3.5:
    print("⭐ Good rating! Satisfied customer")
elif customer_rating >= 2.5:
    print("⭐ Average rating - need improvement")
else:
    print("⭐ Poor rating - something went wrong!")

# Combined quality check
if fish_freshness == "fresh" and customer_rating >= 4.0:
    print("✅ Perfect order! Fresh fish + happy customer!")
elif fish_freshness == "old" or customer_rating < 2.0:
    print("⚠️ Quality alert! Need to check this order!")

print("=" * 40)