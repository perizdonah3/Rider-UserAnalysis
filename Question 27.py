# Question 27 - Normal Horizontal Bar Graph

import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"

df = pd.read_csv(file_path)

# Clean data
df = df.drop_duplicates()
df.columns = df.columns.str.strip()

# Q27 challenge columns
components = [
    "Faulty batteries",
    "Quick battery drainage",
    "Few skilled technicians",
    "Few charging/swapping stations",
    "Unreliable swapping stations",
    "Not enough batteries in swapping stations",
    "Other (specify)"
]

# Count "Yes" responses
counts = []

for component in components:
    column = f"27. What challenges do you face?/{component}"
    count = (
        df[column]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
        .sum()
    )
    counts.append(count)

# Create horizontal bar graph
plt.figure(figsize=(12, 7))

plt.barh(components, counts)

plt.xlabel("Number of Riders")
plt.ylabel("Challenges")
plt.title(" Challenges Faced by Riders")

# Add numbers to bars
for i, value in enumerate(counts):
    if value > 0:
        plt.text(value + 0.5, i, str(value), va="center")

plt.tight_layout()
plt.show()