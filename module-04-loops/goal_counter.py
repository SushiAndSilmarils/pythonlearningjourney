"""
⚽ Goal Counter - For Loop Practice
Using a for loop to accumulate totals across a season, instead of
calling a function once per match like we did in module-03.
"""

# Goals Arsenal scored in each of their last 8 matches
goals_per_match = [3, 1, 2, 0, 4, 1, 2, 5]

total_goals = 0
matches_scored_in = 0
biggest_win_goals = 0

for goals in goals_per_match:
    total_goals = total_goals + goals

    if goals > 0:
        matches_scored_in = matches_scored_in + 1

    if goals > biggest_win_goals:
        biggest_win_goals = goals

print("=" * 40)
print("⚽ ARSENAL — GOAL COUNTER (Last 8 Matches)")
print("=" * 40)
print(f"Match by match: {goals_per_match}")
print(f"Total goals scored: {total_goals}")
print(f"Matches scored in: {matches_scored_in} / {len(goals_per_match)}")
print(f"Average goals per match: {total_goals / len(goals_per_match):.2f}")
print(f"Biggest single-match haul: {biggest_win_goals} goals")
print("=" * 40)
