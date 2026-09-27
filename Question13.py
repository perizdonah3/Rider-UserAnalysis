import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Question 13
column13_name = [
    col for col in df.columns
    if str(col).strip().startswith(
        "13. How often do you use Arc Ride charging/battery swap services?"
    )
][0]

column13 = df[column13_name].dropna().astype(str).str.strip()

# Calculate percentages
column13_percent = column13.value_counts(normalize=True) * 100

# Create horizontal bar graph
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    column13_percent.index,
    column13_percent.values,
    height=0.55,
    color=["green", "blue", "red", "yellow"],
)

# Title and labels
ax.set_title(
    " How often do you use Arc Ride charging/battery swap services?",
    fontsize=14,
    fontweight="bold"
)

ax.set_xlabel("Percentage of Responses (%)")
ax.set_ylabel("Frequency of Use")

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