# Q1)

# Part A

def part_a():
  string_list = []
  integer_list = []

  for i in range(0, 3):
    number = input("Enter a number: ")
    string_list.append(number)

  concatenated = "".join(string_list)

  for i in string_list:
    number = int(i)
    integer_list.append(number)

  total = sum(integer_list)

  # print(concatenated)
  # print(sum(integer_list))
  # print(string_list)

  return(f"{concatenated}\n{total}\n{string_list}")

print(part_a())