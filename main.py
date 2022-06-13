year = int(input("Which year do you wamt to check ?"))
if year % 4 == 0:
  if year %  100 == 0:
    if year % 400 == 0:
      print("A leap year")
    else:
      print("Not a leap year")
  else:
    print("A leap year")
else:
  print("Not a leap year")
