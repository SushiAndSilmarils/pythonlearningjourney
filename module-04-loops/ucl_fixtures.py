"""
⚽ UCL Fixtures - Nested Loops
Using a loop inside another loop to pair every team against every
other team - a classic nested loop use case (round-robin fixtures).
"""

teams = ["Arsenal", "Real Madrid", "Bayern Munich", "PSG"]

print("=" * 40)
print("⚽ CHAMPIONS LEAGUE — FIXTURE GENERATOR")
print("=" * 40)

fixture_count = 0

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f"{home_team}  vs  {away_team}")
            fixture_count = fixture_count + 1

print("-" * 40)
print(f"Total fixtures generated: {fixture_count}")
print(f"({len(teams)} teams x {len(teams) - 1} opponents each)")
print("=" * 40)
