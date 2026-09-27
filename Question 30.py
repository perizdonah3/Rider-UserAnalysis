import matplotlib.pyplot as plt

# Question 30: Barriers to adopting electric motorcycles

barriers = [
    "Battery concerns",
    "Limited awareness",
    "Maintenance concerns",
    "Other",
    "Lack of adequate charging/swap stations",
    "High cost of charging/swapping",
    "Resale challenges",
    "High cost of electric motorcycles",
    "Lack of technicians"
]

counts = [30, 28, 20, 21, 13, 8, 6, 4, 2]

# Calculate percentages
total = sum(counts)
percentages = [(count / total) * 100 for count in counts]

# Create clean horizontal bar graph
fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.barh(
    barriers,
    percentages,
    height=0.6
)

# Add percentages at the end of each bar
for bar, value in zip(bars, percentages):
    ax.text(
        value + 0.3,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.1f}%",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

ax.set_title(
    "Barriers to Adopting Electric Motorcycles",
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax.set_xlabel(
    "Percentage of Respondents (%)",
    fontsize=12
)

ax.set_ylabel(
    "Barriers",
    fontsize=12
)

# Largest bar at the top
ax.invert_yaxis()

plt.tight_layout()
plt.show()