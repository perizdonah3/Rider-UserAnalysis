import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Question 22
column22_name = [
    col for col in df.columns
    if str(col).strip().startswith("22.")
][0]

column22 = df[column22_name].dropna().astype(str).str.strip()

# Calculate percentages
column22_percent = column22.value_counts(normalize=True) * 100

# Create horizontal bar graph
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    column22_percent.index,
    column22_percent.values,
    height=0.55,
    color="steelblue"
)

# Title and labels
ax.set_title(
    "Have you experienced battery shortages or long waiting times?",
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