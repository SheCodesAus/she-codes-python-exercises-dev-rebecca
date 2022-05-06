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

list = []

for item in groceries:
  units = int(input(f"How many units of {item[0]} did you purchase? "))
  list.append(units)
 
print("===Izzy's Food Emporium===")

for item in groceries:
  print(f"{item[0]} {item[1]}")

for amount in list:
  print(amount * item[1])

print("=====================")










# for unit in list:
#   for item in groceries:
#     sub_total = unit * item[1]
#     print(sub_total)





# for item in groceries:
#   for unit in list:
#       unit_to_float = float(unit)
#       item_to_float = float(item[1])
#       # print(type(unit_to_float))
#       # print(type(item_to_float))
#       total = unit_to_float * item_to_float

# print(total)