"""
⚽ Match Winner - Conditional Statements Practice
Predict who wins based on stats!
"""

# Match data
home_team = "Arsenal"
away_team = "Tottenham Hotspur"
home_goals = 4
away_goals = 1

# Determine winner using conditionals
print("=" * 40)
print(f"⚽ {home_team} vs {away_team}")
print("=" * 40)

if home_goals > away_goals:
    winner = home_team
    print(f"🏆 {home_team} wins!")
elif away_goals > home_goals:
    winner = away_team
    print(f"🏆 {away_team} wins!")
else:
    winner = "Draw"
    print("🤝 It's a draw!")

# Bonus: Check if it was a high-scoring game
total_goals = home_goals + away_goals
if total_goals >= 4:
    print("🔥 High-scoring match!")
elif total_goals >= 2:
    print("⚡ Competitive match!")
else:
    print("🧊 Defensive match!")

print(f"Final score: {home_goals} - {away_goals}")
print("=" * 40)