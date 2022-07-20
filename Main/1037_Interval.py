user_input = float(input())

if(user_input >= 0 and user_input <= 100):
  if(user_input >= 0 and user_input <= 25):
    print("Intervalo [0,25]")
  elif(user_input > 25.00001 and user_input <= 50):
    print("Intervalo (25,50]")
  elif(user_input > 50.00001 and user_input <= 75):
    print("Intervalo (50,75]")
  elif(user_input > 75.00001 and user_input <= 100):
    print("Intervalo (75,100]")
else:
  print("Fora de intervalo")