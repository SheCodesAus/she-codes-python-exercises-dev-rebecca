# Q1)

import csv
from typing import Counter
colours = []

with open("csv_files/colours_20_simple.csv") as csv_file:
  reader = csv.reader(csv_file)
  for row in reader:
    colours.append(row)

for colour in colours:
  print(' '.join(colour))

# Q2)

colours = []

with open("csv_files/colours_20_simple.csv") as csv_file:
  reader = csv.reader(csv_file)
  for row in reader:
    colours.append(row)

colours.pop(-0) # Removing "English HEX RGB" title as seen in exercise

for colour in colours:
  print(f"{colour[2]}, {colour[1]}, {colour[0]}")

# Q3)

# Duplicate of Q2

# Q4)

# colours_20.csv

colours = []
red_counter = 0
green_counter = 0
blue_counter = 0
yellow_counter = 0

with open("csv_files/colours_20.csv") as csv_file:
  reader = csv.reader(csv_file)
  for row in reader:
    colours.append(row)

for colour in colours:
  red = colour[4].find("red")
  green = colour[4].find("green")
  blue = colour[4].find("blue")
  yellow = colour[4].find("yellow")

  if red >= 0:
    red_counter += 1
  if green >= 0:
    green_counter += 1
  if blue >= 0:
    blue_counter += 1
  if yellow >= 0:
    yellow_counter += 1

print(f"Red: {red_counter}\nGreen: {green_counter}\nBlue: {blue_counter}\nYellow: {yellow_counter}")

# colours_213.csv

colours = []
red_counter = 0
green_counter = 0
blue_counter = 0
yellow_counter = 0

with open("csv_files/colours_213.csv") as csv_file:
  reader = csv.reader(csv_file)
  for row in reader:
    colours.append(row)

for colour in colours:
  red = colour[4].find("red")
  green = colour[4].find("green")
  blue = colour[4].find("blue")
  yellow = colour[4].find("yellow")

  if red >= 0:
    red_counter += 1
  if green >= 0:
    green_counter += 1
  if blue >= 0:
    blue_counter += 1
  if yellow >= 0:
    yellow_counter += 1

print(f"Red: {red_counter}\nGreen: {green_counter}\nBlue: {blue_counter}\nYellow: {yellow_counter}")

# Q5)

space_info = []
velocities = []
int_velocities = []
galaxies = []

with open("csv_files/galaxies.csv") as csv_file:
  reader = csv.reader(csv_file)
  for row in reader:
      space_info.append(row)

for item in space_info:
  velocities.append(item[1])

velocities.pop(0)

for velocity in velocities:
  int_velocities.append(int(velocity))

minimum = min(int_velocities)
minimum_index = int_velocities.index(minimum)

maximum = max(int_velocities)
maximum_index = int_velocities.index(maximum)

for galaxy in space_info:
  galaxies.append(galaxy[0])

galaxies.pop(0)

print(f"Galaxy {galaxies[minimum_index]} has the min velocity of {minimum}km/sec.")
print(f"Galaxy {galaxies[maximum_index]} has the min velocity of {maximum}km/sec.")
