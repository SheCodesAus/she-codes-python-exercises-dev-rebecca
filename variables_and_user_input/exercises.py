# Q1) Write a program that takes two numbers from the user, and outputs their sum.

first = float(input("Enter a number: "))
second = float(input("Enter another number: "))

result = first + second
print(result)

#Q2) Write a program that takes two numbers from the user, and outputs the equation representing the multiplication of the two numbers.

first = float(input("Enter a number: "))
second = float(input("Enter another number: "))

result = first * second
print(result)

# Q3) Write a program that takes a distance in kilometers from the user, and output the distance in meters and centimeters.

kilometers = (float(input("How many kilometres? ")))

metres = int(kilometers * 1000)
centimetres = int(kilometers * 100000)

print(f"{kilometers}km = {metres}m")
print(f"{kilometers}km = {centimetres}cm")