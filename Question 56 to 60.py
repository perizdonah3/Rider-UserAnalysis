import pandas as pd
import matplotlib.pyplot as plt

file_path = "RiderData.csv"
df = pd.read_csv(file_path)

questions = [
    ("56.", "Respectful Behaviour Information"),
    ("57.", "Misconduct Reporting Posters"),
    ("58.", "Where to Report Harassment"),
    ("59.", "Harassment or Unsafe Behaviour"),
    ("60.", "CSEA at Charging or Swapping Station")
]

for number, title in questions:

    # Find the correct question column
    column_name = [
        col for col in df.columns
        if str(col).strip().startswith(number)
    ][0]

    # Clean responses
    column = (
        df[column_name]
        .dropna()
        .astype(str)
        .str.strip()
    )

    # Remove parentheses and their contents
    column = column.str.replace(
        r"\s*\([^)]*\)",
        "",
        regex=True
    ).str.strip()

    # Calculate percentages
    column_percent = column.value_counts(normalize=True) * 100

    # Create clean horizontal graph
    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.barh(
        column_percent.index,
        column_percent.values,
        height=0.6
    )

    # Add percentages
    for bar in bars:
        value = bar.get_width()

        ax.text(
            value + 0.5,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.1f}%",
            va="center",
            fontsize=10,
            fontweight="bold"
        )

    ax.set_title(
        title,
        fontsize=16,
        fontweight="bold",
        pad=15
    )

    ax.set_xlabel(
        "Percentage of Responses (%)",
        fontsize=12
    )

    ax.set_ylabel(
        "Response",
        fontsize=12
    )

    # Clean appearance
    ax.invert_yaxis()

    plt.tight_layout()
    plt.show()