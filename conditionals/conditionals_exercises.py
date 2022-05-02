# Q1) 

moths_in_house = True

if moths_in_house:
  print("Get the moths!")
else:
  print("No threats detected.")

  #Q2)

mitch_is_home = True

if moths_in_house and mitch_is_home:
  print("Hoooman! Help me get the moths!")
elif not moths_in_house and not mitch_is_home:
  print("No threats detected")
elif moths_in_house and not mitch_is_home:
  print("Meooooooow! Hissss!")
elif not moths_in_house and mitch_is_home:
  print("Climb on Mitch")

  #Q3)

light_colour = "Red"
car_detected = False
nothing = "Do nothing."

if light_colour == "Red" and not car_detected:
  print(nothing)
elif light_colour == "Red" and car_detected:
  print("Flash!")
elif light_colour == "Green" and not car_detected:
  print(nothing)
elif light_colour == "Green" and car_detected:
  print(nothing)
elif light_colour == "Amber" and not car_detected:
  print(nothing)
elif light_colour == "Amber" and car_detected:
  print(nothing)

#Q4)

