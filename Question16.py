import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Question 16
column16_name = [
    col for col in df.columns
    if str(col).strip().startswith("16.")
][0]

column16 = df[column16_name].dropna().astype(str).str.strip()

# Calculate percentages
column16_percent = column16.value_counts(normalize=True) * 100

# Create horizontal bar graph
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    column16_percent.index,
    column16_percent.values,
    height=0.55,
    color=["green", "blue", "yellow", "pink", "orange", "purple","maroon",],
)

# Title and labels
ax.set_title(
    "How far do you travel to reach the nearest station? (Km)",
    fontsize=14,
    fontweight="bold"
)

ax.set_xlabel("Percentage of Responses (%)")
ax.set_ylabel("Response")

# Add percentages
for bar in bars:
    width = bar.get_width()

    ax.text(
        width + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.1f}%",
        ha="left",
        va="center",
        fontsize=9
    )

plt.tight_layout()
plt.show()