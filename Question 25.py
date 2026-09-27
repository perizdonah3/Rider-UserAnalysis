import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = "RiderData.csv"

df = pd.read_csv(file_path)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove spaces from column names
df.columns = df.columns.str.strip()

# Question 25: the 5 components
components = [
    "Battery quality",
    "Charging speed",
    "Customer service",
    "Safety of stations",
    "Reliability of service"
]

# Satisfaction levels
ratings = [
    "Very Poor",
    "Poor",
    "Average",
    "Good",
    "Very Good"
]

# Count each rating
data = {}

for component in components:
    data[component] = (
        df[component]
        .astype(str)
        .str.strip()
        .value_counts()
        .reindex(ratings, fill_value=0)
    )

# Convert to DataFrame
results = pd.DataFrame(data).T

# Calculate percentages for each component
percentages = results.div(results.sum(axis=1), axis=0) * 100

# Create horizontal clustered bar graph
ax = results.plot(
    kind="barh",
    figsize=(12, 7),
    width=0.8
)

# Add percentage labels to the bars
for i, component in enumerate(components):
    for j, rating in enumerate(ratings):
        count = results.loc[component, rating]
        percentage = percentages.loc[component, rating]

        if count > 0:
            ax.text(
                count + 0.5,
                i + (j - 2) * 0.13,
                f"{percentage:.1f}%",
                va="center",
                fontsize=9
            )

plt.title("Satisfaction Ratings")
plt.xlabel("Number of Riders")
plt.ylabel("Satisfaction Component")

plt.legend(
    title="Satisfaction Rating",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

plt.tight_layout()
plt.show()