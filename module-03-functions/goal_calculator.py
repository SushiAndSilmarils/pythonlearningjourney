"""
⚽ Goal Calculator - Functions Practice
Turning the Premier League stats logic from module-01 and module-02
into reusable functions.
"""


def calculate_points(wins, draws):
    """3 points per win, 1 point per draw."""
    return (wins * 3) + draws


def calculate_goal_difference(goals_scored, goals_conceded):
    """Goals scored minus goals conceded."""
    return goals_scored - goals_conceded


def classify_form(points, matches_played):
    """Describe a team's season based on points per game."""
    points_per_game = points / matches_played

    if points_per_game >= 2.2:
        return "title contenders 🏆"
    elif points_per_game >= 1.7:
        return "Champions League chasing 🔵"
    elif points_per_game >= 1.3:
        return "mid-table ⚪"
    else:
        return "relegation battle 🔴"


def match_result(home_team, away_team, home_goals, away_goals):
    """Return the winner of a single match, or 'Draw'."""
    if home_goals > away_goals:
        return home_team
    elif away_goals > home_goals:
        return away_team
    else:
        return "Draw"


def print_team_report(team_name, wins, draws, losses, goals_scored, goals_conceded):
    """Print a full stats report for one team, using the functions above."""
    matches_played = wins + draws + losses
    points = calculate_points(wins, draws)
    goal_diff = calculate_goal_difference(goals_scored, goals_conceded)
    form = classify_form(points, matches_played)

    print("=" * 40)
    print(f"⚽ {team_name.upper()} — SEASON REPORT")
    print("=" * 40)
    print(f"Matches played: {matches_played}")
    print(f"Record: {wins}W - {draws}D - {losses}L")
    print(f"Points: {points}")
    print(f"Goal difference: {goal_diff:+d}")
    print(f"Status: {form}")
    print("=" * 40)


# --- Use the functions ---
print_team_report(
    team_name="Arsenal",
    wins=26,
    draws=7,
    losses=5,
    goals_scored=71,
    goals_conceded=27,
)

# A quick single-match example using match_result()
winner = match_result("Arsenal", "Tottenham Hotspur", home_goals=4, away_goals=1)
print(f"\nMatch result: {winner} wins the North London Derby!")