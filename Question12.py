import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Question 12
column12_name = [
    col for col in df.columns
    if str(col).strip().startswith(
        "12. Approximately how many kilometres do you travel a day?"
    )
][0]

column12 = df[column12_name].dropna().astype(str).str.strip()

# Calculate percentages
column12_percent = column12.value_counts(normalize=True) * 100

# Create horizontal bar graph
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    column12_percent.index,
    column12_percent.values,
    height=0.55,
    color="steelblue"
)

# Title and labels
ax.set_title(
    "Daily Travel Distance",
    fontsize=14,
    fontweight="bold"
)

ax.set_xlabel("Percentage of Responses (%)")
ax.set_ylabel("Distance Travelled Per Day")

# Add percentages at the end of each bar
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