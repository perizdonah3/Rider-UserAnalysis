import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("RiderData.csv")

# Question 37
column_name = [
    col for col in df.columns
    if str(col).strip().startswith("37.")
][0]

column = df[column_name].dropna().astype(str).str.strip()

# Remove parentheses and their contents
column = column.str.replace(
    r"\s*\([^)]*\)", "", regex=True
).str.strip()

# Calculate percentages
column_percent = column.value_counts(normalize=True) * 100

# Create graph
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    column_percent.index,
    column_percent.values,
    height=0.55
)

ax.set_title(
    "Faulty Battery Replacement Time",
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

ax.invert_yaxis()

plt.tight_layout()
plt.show()