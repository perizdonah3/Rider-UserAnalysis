import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

# Questions 53–60
questions = [
    ("53.", "Grievance Redress Mechanism"),
    ("54.", "Complaints Made"),
    ("54b.", "Complaint Resolution"),
    ("56.", "Respectful Behaviour Information"),
    ("57.", "Misconduct Reporting Posters"),
    ("58.", "Where to Report Harassment"),
    ("59.", "Harassment or Unsafe Behaviour"),
    ("60.", "CSEA at Charging/Swapping Station")
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

    # Create horizontal bar graph
    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.barh(
        column_percent.index,
        column_percent.values
    )

    # Title
    ax.set_title(
        title,
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel("Percentage of Responses (%)")
    ax.set_ylabel("Response")

    # Add percentage labels
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