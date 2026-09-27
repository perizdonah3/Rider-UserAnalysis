import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Select Column 1
column1 = df.iloc[:, 0].dropna()

# Remove anything inside brackets
column1 = column1.str.replace(r"\s*\(.*?\)", "", regex=True).str.strip()

# Calculate percentages
column1_percentages = column1.value_counts(normalize=True) * 100

# Create a narrower bar graph
plt.figure(figsize=(8, 5))


column1_percentages.plot(
    kind="bar",
    color=["green", "blue", "red", "yellow"],
    width=0.6
)

# Add titles and labels
plt.title("Urban High-Density Hubs")
plt.xlabel("Hub Location")
plt.ylabel("Percentage of Responses (%)")

# Keep labels readable
plt.xticks(rotation=30, ha="right")

# Add percentage values above each bar
for i, value in enumerate(column1_percentages):
    plt.text(
        i,
        value + 0.5,
        f"{value:.1f}%",
        ha="center"
    )

plt.tight_layout()
plt.show()