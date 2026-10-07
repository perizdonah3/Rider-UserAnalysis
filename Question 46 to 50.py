import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("RiderData.csv")

column_name = [
    col for col in df.columns
    if str(col).strip().startswith("46.")
][0]

column = df[column_name].dropna().astype(str).str.strip()
column = column.str.replace(r"\s*\([^)]*\)", "", regex=True).str.strip()

percentages = column.value_counts(normalize=True) * 100

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(percentages.index, percentages.values)

ax.set_title("Safe Riding Training", fontsize=16, fontweight="bold")
ax.set_xlabel("Percentage of Responses (%)")
ax.set_ylabel("Response")

for bar in bars:
    value = bar.get_width()
    ax.text(
        value + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.1f}%",
        va="center",
        fontweight="bold"
    )

ax.invert_yaxis()
plt.tight_layout()
plt.show()