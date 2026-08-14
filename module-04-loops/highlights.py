"""
⚽ Highlights - Filter Pattern
The "filter" loop pattern: walk through a list and only keep/print
the items that pass a condition, skipping the rest.
"""

matches = ["Arsenal 3-1 Chelsea", "Arsenal 0-0 Burnley", "Arsenal 4-2 Man City",
           "Arsenal 1-0 Everton", "Arsenal 5-1 Sheffield United", "Arsenal 2-2 Newcastle"]
goals_scored = [3, 0, 4, 1, 5, 2]

HIGHLIGHT_THRESHOLD = 3  # games with 3+ goals scored make the highlight reel

print("=" * 40)
print("⚽ ARSENAL — MATCH HIGHLIGHTS REEL")
print("=" * 40)

highlight_count = 0

for i in range(len(matches)):
    if goals_scored[i] >= HIGHLIGHT_THRESHOLD:
        print(f"🔥 {matches[i]}")
        highlight_count = highlight_count + 1
    # games below the threshold are simply skipped - that's the filter

print("-" * 40)
print(f"{highlight_count} out of {len(matches)} matches made the highlight reel")
print("=" * 40)
