import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Select Question 11: How often do you use your electric motorcycle?
column11 = df.iloc[:, 22].dropna().astype(str)

# Clean the responses
column11 = column11.str.strip()

# Calculate percentages
column11_percent = column11.value_counts(normalize=True) * 100

# Create graph
fig, ax = plt.subplots(figsize=(10, 6))

y = np.arange(len(column11_percent))

# Bar thickness
height = 0.5

# Create horizontal bars
bars = ax.barh(
    y,
    column11_percent.values,
    height=height,
    color="steelblue"
)

# Title
ax.set_title(
    "How Often Do You Use Your Electric Motorcycle?",
    fontsize=14,
    fontweight="bold"
)

# X-axis
ax.set_xlabel("Percentage of Responses (%)")

# Y-axis
ax.set_ylabel("Frequency of Use")

# Y-axis labels
ax.set_yticks(y)
ax.set_yticklabels(column11_percent.index)

# Add percentages at the end of bars
for bar in bars:
    width_value = bar.get_width()

    ax.text(
        width_value + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{width_value:.1f}%",
        ha="left",
        va="center",
        fontsize=9
    )

# Make everything fit nicely
plt.tight_layout()

# Display graph
plt.show()