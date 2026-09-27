import pandas as pd
import matplotlib.pyplot as plt

from Question11 import df

# Q37
column = "37. How quickly are faulty batteries replaced?"

# Count each response
counts = df[column].value_counts()

# Horizontal bar graph
plt.figure(figsize=(10, 6))

bars = plt.barh(counts.index, counts.values)

# Add values at the end of each bar
for bar, value in zip(bars, counts.values):
    plt.text(
        value + 0.5,
        bar.get_y() + bar.get_height() / 2,
        str(value),
        va="center"
    )

plt.xlabel("Number of Respondents")
plt.ylabel("Replacement Speed")
plt.title("How Quickly Are Faulty Batteries Replaced?")

plt.tight_layout()
plt.show()