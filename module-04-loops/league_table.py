"""
⚽ League Table - While Loop Practice
Simulating a season matchday by matchday with a while loop, since we
don't know in advance exactly how many matches it'll take to reach
a target points total (a good use case for while over for).
"""

# Arsenal's results this season so far, in order: "W", "D", or "L"
season_results = ["W", "W", "D", "L", "W", "W", "D", "W", "L", "W"]

matchday = 0
points = 0
target_points = 20

print("=" * 40)
print("⚽ ARSENAL — SEASON SIMULATION")
print("=" * 40)

while points < target_points and matchday < len(season_results):
    result = season_results[matchday]
    matchday = matchday + 1

    if result == "W":
        points = points + 3
    elif result == "D":
        points = points + 1
    # a loss adds 0 points

    print(f"Matchday {matchday}: {result}  -->  {points} points")

print("=" * 40)

if points >= target_points:
    print(f"🎯 Target of {target_points} points reached after {matchday} matchdays!")
else:
    print(f"Season data ran out at {points} points after {matchday} matchdays.")

print("=" * 40)
