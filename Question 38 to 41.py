import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Questions 38–41
questions = [
    ("38.", "Injuries Around Swap Stations"),
    ("39.", "Pedestrian Protection"),
    ("40.", "Station Accessibility"),
    ("41.", "Children Near Charging Equipment")
]

for number, title in questions:

    # Find the correct column automatically
    column_name = [
        col for col in df.columns
        if str(col).strip().startswith(number)
    ][0]

    # Get responses
    column = df[column_name].dropna().astype(str).str.strip()

    # Calculate percentages
    column_percent = column.value_counts(normalize=True) * 100

    # Create pie chart
    fig, ax = plt.subplots(figsize=(7, 7))

    ax.pie(
        column_percent.values,
        labels=column_percent.index,
        autopct="%1.1f%%",
        startangle=90
    )

    # Title
    ax.set_title(
        title,
        fontsize=14,
        fontweight="bold"
    )

    plt.tight_layout()
    plt.show()