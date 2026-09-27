import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Question 4 and Question 5
questions = [
    ("4.", "Occupation"),
    ("5.", "Age")
]

for number, title in questions:

    # Find the correct column automatically
    column_name = [
        col for col in df.columns
        if str(col).strip().startswith(number)
    ][0]

    # Get responses
    column = df[column_name].dropna().astype(str).str.strip()

    # Remove parentheses and their contents
    column = column.str.replace(r"\s*\([^)]*\)", "", regex=True).str.strip()

    # Calculate percentages
    column_percent = column.value_counts(normalize=True) * 100

    # Create pie chart
    fig, ax = plt.subplots(figsize=(8, 8))

    wedges, texts, autotexts = ax.pie(
        column_percent.values,
        labels=column_percent.index,
        autopct="%1.1f%%",
        startangle=90,
        pctdistance=0.72,
        labeldistance=1.08,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5}
    )

    # Make percentage labels clear
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight("bold")

    # Title
    ax.set_title(
        title,
        fontsize=16,
        fontweight="bold",
        pad=20
    )

    ax.axis("equal")

    plt.tight_layout()
    plt.show()