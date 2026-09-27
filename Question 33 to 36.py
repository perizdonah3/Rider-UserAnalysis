import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

questions = [
    ("", "Battery Lasts as Expected"),
    ("", "Battery Overheating"),
    ("", "Battery Failure While Riding"),
    ("", "Received Damaged Battery")
]

# Store percentages
all_data = []

for number, title in questions:

    # Find the correct column
    column_name = [
        col for col in df.columns
        if str(col).strip().startswith(number)
    ][0]

    # Clean the responses
    column = (
        df[column_name]
        .dropna()
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # Calculate percentages
    percentages = column.value_counts(normalize=True) * 100

    all_data.append(percentages)

# Get all response categories found
responses = sorted(
    set().union(*[set(data.index) for data in all_data])
)

# Create graph
fig, ax = plt.subplots(figsize=(12, 7))

y = range(len(questions))
height = 0.8 / len(responses)

for i, response in enumerate(responses):

    values = [
        data.get(response, 0)
        for data in all_data
    ]

    positions = [
        j + (i - (len(responses) - 1) / 2) * height
        for j in y
    ]

    bars = ax.barh(
        positions,
        values,
        height=height,
        label=response.capitalize()
    )

    # Add percentages
    for bar, value in zip(bars, values):
        if value > 0:
            ax.text(
                value + 0.5,
                bar.get_y() + bar.get_height() / 2,
                f"{value:.1f}%",
                va="center",
                fontsize=9,
                fontweight="bold"
            )

ax.set_yticks(y)
ax.set_yticklabels([title for _, title in questions])

ax.set_xlabel(
    "Percentage of Respondents (%)",
    fontsize=12
)

ax.set_ylabel(
    "Questions",
    fontsize=12
)

ax.set_title(
    "Battery Performance and Condition",
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax.legend(title="Response")

ax.invert_yaxis()

plt.tight_layout()
plt.show()