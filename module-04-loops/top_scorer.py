"""
⚽ Top Scorer - Search Pattern
The classic "find the largest value" loop pattern: walk through a list,
keep track of the best one seen so far, and update it when you find
something better.
"""

players = ["Saka", "Havertz", "Odegaard", "Martinelli", "Trossard"]
goals = [12, 9, 7, 10, 6]

# Search pattern: start with a "smallest possible" guess, then update
top_scorer_name = None
top_scorer_goals = -1

position = 0
for goals_scored in goals:
    if goals_scored > top_scorer_goals:
        top_scorer_goals = goals_scored
        top_scorer_name = players[position]
    position = position + 1

print("=" * 40)
print("⚽ ARSENAL — TOP SCORER SEARCH")
print("=" * 40)
for i in range(len(players)):
    print(f"{players[i]}: {goals[i]} goals")
print("-" * 40)
print(f"🏆 Top scorer: {top_scorer_name} with {top_scorer_goals} goals")
print("=" * 40)
