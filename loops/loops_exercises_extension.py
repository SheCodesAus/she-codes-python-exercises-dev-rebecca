# Q1)

# The items and how much they cost
groceries = [
  ["Baby Spinach", 2.78],
  ["Hot Chocolate", 3.70],
  ["Crackers", 2.10],
  ["Bacon", 9.00],
  ["Carrots", 0.56],
  ["Oranges", 3.08]
]

# Asks user how many of each item they purchased and stores in a new list called units_bought
units_bought = []

for item in groceries:
  each_unit = input(f"How many units of {item[0]} did you purchase? ")
  units_bought.append(each_unit)

# Print how much each item costs
for cost in groceries:
  total_cost = cost[1]
  print(total_cost)

# Print how much the person said they bought
for quantity in units_bought:
  final_quantity = quantity[0]
  print(final_quantity)

# Mulitply how many units were purchased by the amount the item costs
  # total = (float(total_cost) * float(final_quantity))
  # print(total)

# print(total_cost)
# print(final_quantity)

# total = (float(total_cost)*float(final_quantity))
# print(total)

# print(units_bought[0] * )