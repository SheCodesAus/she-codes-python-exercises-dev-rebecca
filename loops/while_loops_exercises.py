# Q1)
# I acknowledge that I probably did this in the worst/longest possible way

number = "not nothing"
list = []

while number != "":
  number = input("Enter a number: ")
  list.append(number)

list.pop()
list = [int(i) for i in list] # List comprehension - recreating the list with int instead of str
print(sum(list))

# Q2)

# Not sure how to do this with a while loop instead of for loop
number = int(input("Enter a number: "))
for num in range(1, number, 2):
  print(num)

# Q3)

number = 10
guess = ""

while guess != number:
  guess = int(input("Guess a number: "))

  if guess > number:
    print("Too high!")
  if guess < number:
    print("Too low!")
  if guess == number:
    print("Correct!")
