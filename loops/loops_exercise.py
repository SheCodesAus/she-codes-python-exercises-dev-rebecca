# Q1)

# Ask user for a number
user_number = int(input("Enter a number: "))

# Create list of numbers, ending with number user specified
for i in range(1, user_number + 1):
  # Print calculation and results
  print(f"{user_number} * {i} = {user_number * i}")