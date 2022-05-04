# Q1)

user_number = int(input("Enter a number: "))

for i in range(1, user_number + 1):
  print(f"{user_number} * {i} = {user_number * i}")

# Q3)

random_numbers = [3, 5, 9, 1]
sum = 0

for number in random_numbers:
  sum = sum + number
  
print(sum)

# Q4)

mailing_list = [
  ["Chilli", "chilli@thechihuahua.com"],
  ["Roary", "roary@moth.catchers"],
  ["Remus", "remus@kapers.dog"],
  ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
  ["Ivy", "noreply@goldendreamers.xyz"],
]

for items in mailing_list:
  print(f"{items[0]}: {items[1]}")
