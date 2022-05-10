# Q1)

def fahrenheit_to_celcius(fahrenheit):
  celcius = 5/9 * (fahrenheit - 32)
  return celcius

print(fahrenheit_to_celcius(32))

# Q2)

def even_or_odd(number):
  if number % 2 == 0:
    return False
  else:
    return True

print(even_or_odd(0))

# Q3)

def mean_calculator(numbers):
  length = len(numbers)
  mean = sum(numbers) / length
  return mean

print(mean_calculator([4, 3, 2, 6]))

# Q4

def cost_calculator(price_per_unit, num_units):
  total = f"${price_per_unit * num_units}"
  return total

print(cost_calculator(4.25, 3))