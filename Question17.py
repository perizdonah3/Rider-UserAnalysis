import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Question 17
column17_name = [
    col for col in df.columns
    if str(col).strip().startswith("17.")
][0]

column17 = df[column17_name].dropna().astype(str).str.strip()

# Calculate percentages
column17_percent = column17.value_counts(normalize=True) * 100

# Create horizontal bar graph
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    column17_percent.index,
    column17_percent.values,
    height=0.55,
    color="steelblue"
)

# Title and labels
ax.set_title(
    " How long does the battery swap/charging process usually take?",
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