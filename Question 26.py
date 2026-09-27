import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = "RiderData.csv"

df = pd.read_csv(file_path)

# Remove duplicates
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.strip()

# Question 26
column = "26.  What are the biggest benefits of using an electric motorcycle?"

# Count the responses
benefits = df[column].astype(str).str.strip().value_counts()

# Create horizontal bar graph
plt.figure(figsize=(10, 6))

plt.barh(
    benefits.index,
    benefits.values
)

plt.xlabel("Number of Riders")
plt.ylabel("Benefits")
plt.title(" Biggest Benefits of Using an Electric Motorcycle")

# Display the values at the end of each bar
for i, value in enumerate(benefits.values):
    plt.text(value + 0.5, i, str(value), va="center")

plt.tight_layout()
plt.show()