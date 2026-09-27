import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Select Column 2
column2 = df.iloc[:, 1].dropna()

# Remove anything inside brackets
column2 = column2.str.replace(r"\s*\(.*?\)", "", regex=True).str.strip()

# Calculate percentages
column2_percentages = column2.value_counts(normalize=True) * 100

# Create a narrower bar graph
plt.figure(figsize=(8, 5))

column2_percentages.plot(
    kind="bar",
    color=["green", "purple", "orange", "yellow"],
    width=0.6
)

# Title and labels
plt.title("Peri-Urban & Commuter Corridors")
plt.xlabel("Location")
plt.ylabel("Percentage of Responses (%)")

# Make labels readable
plt.xticks(rotation=30, ha="right")

# Add percentage values
for i, value in enumerate(column2_percentages):
    plt.text(
        i,
        value + 0.5,
        f"{value:.1f}%",
        ha="center"
    )

plt.tight_layout()
plt.show()