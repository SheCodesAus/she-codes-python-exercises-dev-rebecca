# Q1)

groceries = [
  ["Baby Spinach", 2.78],
  ["Hot Chocolate", 3.70],
  ["Crackers", 2.10],
  ["Bacon", 9.00],
  ["Carrots", 0.56],
  ["Oranges", 3.08]
]

list = []
new_list = []
counter = 0

# Ask user how many of each item and put into a list
for item in groceries:
  units = int(input(f"How many units of {item[0]} did you purchase? "))
  list.append(units)

# Get length of that list
length = len(list)

# Convert list items to float
for amount in list:
  amount = float(amount)

print("====Izzy's Food Emporium====")

# For as long as the list is, use the index of counter to iterate through user specified amounts
while counter < length:
  for item in groceries:
    total = item[1] * list[counter]
    format_total = "{:.2f}".format(total) # Force float to 2 decimal places
    print(f"{item[0]} {format_total}")
    counter += 1

    new_list.append(total) # Put totals in list for summing

grand_total = "{:.2f}".format(sum(new_list)) # Sums totals and formats to 2 decimal places

print(f"=========================\n{grand_total}")

# Q2)

string = input("Please enter a string: ")
length = len(string)
counter = 0

while counter < length:
  print(counter, string[counter])
  counter += 1

# Q3)

number = int(input("Enter a number: "))

print(f"Pyramid size: {number}")

for i in range(0, number):
  stars = i + 1
  print("*" * stars)

# Q4)

# Getting stars 

number = int(input("Enter a number: "))
spaces_list = []
stars_list = []
counter = 0

print(f"Pyramid size: {number}")

for i in range(0, number):
  stars = i + 1 # Get as many lines of stars as the user requested
  amount = "*" * stars # Add more stars for each line
  multiplied = amount * 2 # Double the amount
  removed_one = multiplied[:-1] # Remove one

  stars_list.append(removed_one) # Add the result to a list for use with the spaces

  spaces = removed_one.replace("*", " ") # Copying the stars list but making them spaces
  spaces_list.append(spaces) # Putting them into their own list

while counter < number:
  for i in reversed(spaces_list): # Invert the list
    counter += 1
    extra = counter * " " # Get extra spaces based on index, to make the pyramid centred
    print(extra, i, stars_list[counter -1]) # Put it all together!
