"""
⚽ Premier League Stats - Variables Practice
"""

# Team data
team_name = "Arsenal"
wins = 26
draws = 7
losses = 5
goals_scored = 71
goals_conceded = 27
clean_sheets = 19

# Calculations
total_matches = wins + draws + losses
goal_difference = goals_scored - goals_conceded
points = (wins * 3) + draws

# Print the stats
print("=" * 40)
print("⚽ ENGLISH PREMIER LEAGUE ")
print("📅 2025/2026 SEASON STATS")
print("=" * 40)
print(f"Team: {team_name}")
print(f"Matches played: {total_matches}")
print(f"Wins: {wins}")
print(f"Draws: {draws}")
print(f"Losses: {losses}")
print(f"Points: {points}")
print(f"Goals scored: {goals_scored}")
print(f"Goals conceded: {goals_conceded}")
print(f"Goal difference: {goal_difference}")
print(f"Clean sheets: {clean_sheets}")
print("=" * 40)