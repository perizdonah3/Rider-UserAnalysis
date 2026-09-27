import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Question 15
column15_name = [
    col for col in df.columns
    if str(col).strip().startswith("15.")
][0]

column15 = df[column15_name].dropna().astype(str).str.strip()

# Calculate percentages
column15_percent = column15.value_counts(normalize=True) * 100

# Create horizontal bar graph
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    column15_percent.index,
    column15_percent.values,
    height=0.55,
    color=["green", "blue", "black", "red", "yellow", "purple",],
)

# Title and labels
ax.set_title(
    "Why do you prefer this station?",
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