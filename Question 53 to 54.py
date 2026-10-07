import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("RiderData.csv")

questions = [
    ("53.", "Grievance Redress Mechanism"),
    ("54.", "Complaints Lodged")
]

fig, ax = plt.subplots(figsize=(12, 7))

all_labels = []
all_values = []
all_positions = []

position = 0

for number, title in questions:

    column_name = [
        col for col in df.columns
        if str(col).strip().startswith(number)
    ][0]

    column = df[column_name].dropna().astype(str).str.strip()

    # Remove parentheses and their contents
    column = column.str.replace(
        r"\s*\([^)]*\)", "", regex=True
    ).str.strip()

    # Calculate percentages
    column_percent = column.value_counts(normalize=True) * 100

    for response, percentage in column_percent.items():
        all_labels.append(f"{title}: {response}")
        all_values.append(percentage)
        all_positions.append(position)
        position += 1

    # Add space between questions
    position += 0.5

bars = ax.barh(
    all_positions,
    all_values,
    height=0.55
)

ax.set_yticks(all_positions)
ax.set_yticklabels(all_labels)

ax.set_title(
    "Grievance Mechanism and Complaints",
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Percentage of Responses (%)")
ax.set_ylabel("Question and Response")

# Add percentages
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.1f}%",
        ha="left",
        va="center",
        fontsize=9,
        fontweight="bold"
    )

ax.invert_yaxis()

plt.tight_layout()
plt.show()