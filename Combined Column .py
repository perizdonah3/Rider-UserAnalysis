import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Select the first 3 columns
column1 = df.iloc[:, 0].dropna().astype(str)
column2 = df.iloc[:, 1].dropna().astype(str)
column3 = df.iloc[:, 2].dropna().astype(str)

# Remove anything inside brackets
column1 = column1.str.replace(r"\s*\(.*?\)", "", regex=True).str.strip()
column2 = column2.str.replace(r"\s*\(.*?\)", "", regex=True).str.strip()
column3 = column3.str.replace(r"\s*\(.*?\)", "", regex=True).str.strip()

# Calculate percentages
column1_percent = column1.value_counts(normalize=True) * 100
column2_percent = column2.value_counts(normalize=True) * 100
column3_percent = column3.value_counts(normalize=True) * 100

# Combine all categories
all_categories = sorted(
    set(column1_percent.index)
    | set(column2_percent.index)
    | set(column3_percent.index)
)

# Put the percentages into one table
data = pd.DataFrame({
    "Urban High-Density Hubs": column1_percent,
    "Peri-Urban & Commuter Corridors": column2_percent,
    "Logistics & Fleet Clusters": column3_percent
}).fillna(0)

# Create graph
fig, ax = plt.subplots(figsize=(11, 8))

y = np.arange(len(data))

# Bar thickness
height = 0.28

# Three horizontal bars for each location/category
bars1 = ax.barh(
    y - height,
    data["Urban High-Density Hubs"],
    height,
    label="Urban High-Density Hubs",
    color="blue"
)

bars2 = ax.barh(
    y,
    data["Peri-Urban & Commuter Corridors"],
    height,
    label="Peri-Urban & Commuter Corridors",
    color="green"
)

bars3 = ax.barh(
    y + height,
    data["Logistics & Fleet Clusters"],
    height,
    label="Logistics & Fleet Clusters",
    color="purple"
)

# Title and labels
ax.set_title(
    "Site Topology",
    fontsize=14,
    fontweight="bold"
)

# Percentage values on X-axis
ax.set_xlabel("Percentage of Responses (%)")

# Location categories on Y-axis
ax.set_ylabel("Location / Site Category")

# Y-axis labels
ax.set_yticks(y)
ax.set_yticklabels(data.index)

# Add percentages at the end of bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        width_value = bar.get_width()

        if width_value > 0:
            ax.text(
                width_value + 0.5,
                bar.get_y() + bar.get_height() / 2,
                f"{width_value:.1f}%",
                ha="left",
                va="center",
                fontsize=8
            )

# Legend
ax.legend()

# Make everything fit nicely
plt.tight_layout()

# Display graph
plt.show()