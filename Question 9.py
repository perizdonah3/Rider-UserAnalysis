import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Question 9
column_name = [
    col for col in df.columns
    if str(col).strip().startswith("9.")
][0]

column = df[column_name].dropna().astype(str).str.strip()

# Remove parentheses and their contents
column = column.str.replace(r"\s*\([^)]*\)", "", regex=True).str.strip()

# Calculate percentages
column_percent = column.value_counts(normalize=True) * 100

# Create clean horizontal bar graph
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    column_percent.index,
    column_percent.values
)

ax.set_title(
    "Length of Time Operating as a Rider",
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Percentage of Responses (%)")
ax.set_ylabel("Length of Time")

# Add percentages
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.1f}%",
        ha="left",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

plt.tight_layout()
plt.show()