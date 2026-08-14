"""
🍣⚽ Sushi & Soccer Stats - Combined Loop Practice
Match day at the sushi bar - combining for loops, while loops, search,
and filter patterns in one script, on both themes at once.
"""

# --- For loop: total sushi rolls sold on match days ---
rolls_sold_per_matchday = [45, 60, 38, 72, 55]

total_rolls = 0
for rolls in rolls_sold_per_matchday:
    total_rolls = total_rolls + rolls

print("=" * 40)
print("🍣 MATCHDAY SUSHI SALES (For Loop)")
print("=" * 40)
print(f"Sales by matchday: {rolls_sold_per_matchday}")
print(f"Total rolls sold: {total_rolls}")
print(f"Average per matchday: {total_rolls / len(rolls_sold_per_matchday):.1f}")

# --- Search pattern: busiest matchday ---
busiest_day_index = 0
for i in range(len(rolls_sold_per_matchday)):
    if rolls_sold_per_matchday[i] > rolls_sold_per_matchday[busiest_day_index]:
        busiest_day_index = i

print(f"🔥 Busiest matchday: #{busiest_day_index + 1} with {rolls_sold_per_matchday[busiest_day_index]} rolls")
print("=" * 40)

# --- Filter pattern: only "big match" days (60+ rolls) ---
print()
print("=" * 40)
print("🍣 BIG MATCH DAYS (Filter — 60+ rolls sold)")
print("=" * 40)
for i in range(len(rolls_sold_per_matchday)):
    if rolls_sold_per_matchday[i] >= 60:
        print(f"Matchday #{i + 1}: {rolls_sold_per_matchday[i]} rolls sold 🔥")
print("=" * 40)

# --- While loop: restocking simulation ---
print()
print("=" * 40)
print("🍣 RESTOCKING SIMULATION (While Loop)")
print("=" * 40)

stock = 100
rolls_needed = total_rolls
deliveries = 0

while stock < rolls_needed:
    stock = stock + 40
    deliveries = deliveries + 1
    print(f"Delivery #{deliveries}: stock now at {stock}")

print(f"✅ Enough stock ({stock}) for the season's {rolls_needed} rolls after {deliveries} deliveries")
print("=" * 40)
