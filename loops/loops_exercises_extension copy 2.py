# Q1)

# The items and how much they cost
# groceries = [
#   ["Baby Spinach", 2.78],
#   ["Hot Chocolate", 3.70],
#   ["Crackers", 2.10],
#   ["Bacon", 9.00],
#   ["Carrots", 0.56],
#   ["Oranges", 3.08]
# ]

# list = []

# for item in groceries:
#   units = int(input(f"How many units of {item[0]} did you purchase? "))
#   list.append(units)
#   # print(list)
#   # print(item[1])

# for item in groceries:
#   for amount in list:
#     amount_to_int = float(amount)
#     total = amount_to_int * item[1]
#     new_total = int(total)
#     # print(total)   

# for i in new_total:
#   print(i) 

# Q2)

string = input("Please enter a string: ")
length = len(string)
counter = 0

for i in string:
  print(i)

for i in range(length):
  print(i)

while counter < length:
  print()