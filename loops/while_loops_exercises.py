# Q1)
# I acknowledge that I probably did this in the worst/longest possible way

number = "not nothing"
list = []

while number != "":
  number = input("Enter a number: ")
  list.append(number)

list.pop()
list = [int(i) for i in list]
print(sum(list))
