colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}


colours = [
    "purple",
    "red",
    "yellow",
    "blue",
    "purple",
    "orange",
    "blue",
    "purple",
    "orange",
    "green"
]

# colours = [
#     "orange",
#     "purple",
#     "blue",
#     "yellow",
#     "green",
#     "green",
#     "purple",
#     "purple",
#     "green",
#     "blue",
#     "green",
#     "orange",
#     "purple",
#     "blue",
#     "green",
#     "orange",
#     "orange",
#     "red",
#     "yellow",
#     "yellow"
# ]

for colour in colours:
    if colour == "blue":
        colour_counts["blue"] += 1
    if colour == "green":
        colour_counts["green"] += 1
    if colour == "yellow":
        colour_counts["yellow"] += 1
    if colour == "red":
        colour_counts["red"] += 1
    if colour == "purple":
        colour_counts["purple"] += 1
    if colour == "orange":
        colour_counts["orange"] += 1
    print(f"{colour}: {colour_counts[colour]}")

