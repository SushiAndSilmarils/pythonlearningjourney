# 🐍 Python Learning Journey

> _"From sushi counter to AI engineer — one commit at a time."_  
> — Sushi & Silmarils 🧝

---

## 📖 About This Repository

Welcome to my **Python Learning Journey**! I'm a sushi chef working 7 days a week in Illinois, learning Python through Coursera's **Python for Everybody** specialization. My goal is to transition into AI/ML Engineering.

**"Sushi today, Silmarils tomorrow."**

This repo documents everything I learn — from basic variables to complex algorithms — all themed around my passions:

- 🍣 **Sushi** (my craft)
- ⚽ **Premier League & UCL** (my obsession)
- 🎻 **Violin** (Suzuki Book 4 completed!)
- 🧝 **Lord of the Rings** (my inspiration)

---

## 📚 Course Progress

| Course       | Module   | Topic                           | Status         |
| ------------ | -------- | ------------------------------- | -------------- |
| **Course 1** | Module 1 | Variables & Expressions         | ✅ Complete    |
| **Course 1** | Module 2 | Conditional Execution           | ✅ Complete    |
| **Course 1** | Module 3 | Functions                       | ✅ Complete    |
| **Course 1** | Module 4 | Loops & Iteration               | 🔄 **Active**  |
| **Course 1** | Module 5 | Strings                         | 📅 Next        |
| **Course 2** | -        | Python Data Structures          | 📅 Coming Soon |
| **Course 3** | -        | Using Python to Access Web Data | 📅 Coming Soon |
| **Course 4** | -        | Using Databases with Python     | 📅 Coming Soon |

---

## 📂 Repository Structure

python-learning-journey/
│
├── 📁 module-01-variables/
│ ├── sushi_orders.py # Variables practice
│ └── premier_league_vars.py # Soccer variables
│
├── 📁 module-02-conditionals/
│ ├── match_winner.py # If/else soccer logic
│ └── sushi_quality.py # Conditional quality checks
│
├── 📁 module-03-functions/
│ ├── goal_calculator.py # Soccer functions
│ └── sushi_roll_counter.py # Sushi inventory functions
│
├── 📁 module-04-loops/
│ ├── goal_counter.py # For loop — goal counting
│ ├── league_table.py # While loop — season simulation
│ ├── top_scorer.py # Search pattern
│ ├── highlights.py # Filter pattern
│ ├── ucl_fixtures.py # Nested loops
│ └── sushi_soccer_stats.py # Combined practice
│
├── 📁 practice/
│ └── daily_exercises/ # Daily practice scripts
│
├── 📁 resources/
│ ├── cheatsheet.md # Python quick reference
│ └── coursera_notes.md # Course notes
│
└── 📄 README.md # You are here!

---

## 🎯 What I've Learned So Far

### Module 1: Variables & Expressions ✅

**Key Concepts:**

- Variables and data types (strings, integers, floats, booleans)
- Expressions and statements
- Basic arithmetic operations

**Projects:**

- 🍣 `sushi_orders.py` — Sushi order receipt with calculations
- ⚽ `premier_league_vars.py` — Team statistics

```python
# Example from sushi_orders.py
customer_name = "Aragorn"
order_type = "California Roll"
quantity = 3
price_per_roll = 5.99
total_price = quantity * price_per_roll
```

Module 2: Conditional Execution ✅
Key Concepts:

if / elif / else statements

Boolean logic

Comparison operators (>, <, ==, !=, etc.)

Projects:

⚽ match_winner.py — Predict match winners

🍣 sushi_quality.py — Check ingredient freshness

```python

# Example from match_winner.py

if home_goals > away_goals:
winner = home_team
elif away_goals > home_goals:
winner = away_team
else:
winner = "Draw"
```

# 📁 Module 3: Functions ✅

Turning repeated logic from Module 1 (variables) and Module 2 (conditionals)
into reusable, callable functions.

---

## 🎯 Key Concepts

- Defining functions with `def`
- Parameters and return values
- Calling one function from inside another
- Breaking a big script into small, testable pieces

---

## 📜 Scripts

| File                    | Theme             | What it practices                                                                     |
| ----------------------- | ----------------- | ------------------------------------------------------------------------------------- |
| `goal_calculator.py`    | ⚽ Premier League | Functions for points, goal difference, and season form, combined into one team report |
| `sushi_roll_counter.py` | 🍣 Sushi          | Functions for tracking roll inventory and revenue                                     |

---

## 💡 Example

Before (Module 2 style — logic repeated inline):

```python
points = (wins * 3) + draws
goal_diff = goals_scored - goals_conceded
```

After (Module 3 style — logic wrapped in reusable functions):

```python
def calculate_points(wins, draws):
    return (wins * 3) + draws

def calculate_goal_difference(goals_scored, goals_conceded):
    return goals_scored - goals_conceded

points = calculate_points(26, 7)
goal_diff = calculate_goal_difference(71, 27)
```

The win: `calculate_points()` can now be reused for _any_ team, any
number of times, without retyping the math.

---

## 🏆 Sample Output

```
========================================
⚽ ARSENAL — SEASON REPORT
========================================
Matches played: 38
Record: 26W - 7D - 5L
Points: 85
Goal difference: +44
Status: title contenders 🏆
========================================
```

---

## ⏭️ Next: Module 4 — Loops & Iteration

Repeating this logic across a _list_ of teams instead of calling the
function once per team.
