import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Find Question 12
Question12_name = [
    col for col in df.columns
    if "Approximately how many kilometres do you travel a day?" in str(col)
][0]

# Find Question 13
Question13_name = [
    col for col in df.columns
    if "How often do you use Arc Ride charging/battery swap services?" in str(col)
][0]

# Keep only rows where both questions have answers
data = df[[Question12_name, Question13_name]].dropna()

# Convert categories to numerical codes
q12_categories = data[Question12_name].astype(str).str.strip().unique()
q13_categories = data[Question13_name].astype(str).str.strip().unique()

q12_map = {value: i + 1 for i, value in enumerate(q12_categories)}
q13_map = {value: i + 1 for i, value in enumerate(q13_categories)}

data["Q12_numeric"] = (
    data[Question12_name].astype(str).str.strip().map(q12_map)
)

data["Q13_numeric"] = (
    data[Question13_name].astype(str).str.strip().map(q13_map)
)

# Create scatter plot
plt.figure(figsize=(10, 6))

plt.scatter(
    data["Q12_numeric"],
    data["Q13_numeric"],
    alpha=0.7
)

plt.title(
    "Daily Travel Distance vs Arc Ride Charging/Swap Frequency",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Daily Travel Distance (Q12)")
plt.ylabel("Charging/Battery Swap Frequency (Q13)")

# Show the actual category names on the axes
plt.xticks(
    range(1, len(q12_categories) + 1),
    q12_categories,
    rotation=30,
    ha="right"
)

plt.yticks(
    range(1, len(q13_categories) + 1),
    q13_categories
)

plt.tight_layout()
plt.show()