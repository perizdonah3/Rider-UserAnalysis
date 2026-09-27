import matplotlib.pyplot as plt

# Q32: Policy changes that would encourage wider adoption
themes = [
    "Lower bike/lease cost",
    "Improve battery quality/capacity",
    "Government regulation/support",
    "Lower charging/swap cost",
    "Increase awareness/training",
    "More charging/swap stations",
    "Safety/infrastructure",
    "Customer service/access"
]

counts = [31, 19, 11, 10, 8, 6, 4, 1]

plt.figure(figsize=(12, 7))

bars = plt.barh(themes, counts)

# Add values at the end of each bar
for bar, value in zip(bars, counts):
    plt.text(
        value + 0.3,
        bar.get_y() + bar.get_height() / 2,
        str(value),
        va="center"
    )

plt.xlabel("Number of Responses")
plt.ylabel("Policy Change")
plt.title("Policy Changes That Would Encourage Wider Adoption")

plt.tight_layout()
plt.show()