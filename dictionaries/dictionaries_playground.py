groceries = {"Baby Spinach": 2.78,"Hot Chocolate": 3.70,"Crackers": 2.10,"Bacon": 9.00,"Carrots": 0.56,"Oranges": 3.08,}

groceries["Avocadoes"] = 1.00
print(groceries)

groceries["Hot Chocolate"] = 2.70
print(groceries)

for item in groceries:
  # print(f"{item}: ${groceries[item]}")
  # print(item)
  print(groceries[item])