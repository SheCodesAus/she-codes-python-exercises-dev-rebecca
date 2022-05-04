# Q1)

# Ask user for a number
user_number = int(input("Enter a number: "))

# Create list of numbers, ending with number user specified
for i in range(1, user_number + 1):
  # Print calculation and results
  print(f"{user_number} * {i} = {user_number * i}")

# Q3)

random_numbers = [3, 5, 9, 1]

for number in random_numbers:
  sum = 0
  sum = sum + number
  print(sum)
