user_input = input().split()

A, B, C, D = int(float(user_input[0])), int(float(user_input[1])), int(float(user_input[2])), int(float(user_input[3]))

if B > C and D > A:
  if C + D > A + B:
    if C > 0 and D > 0 and A %2 == 0:
      print("Valores aceitos")
    else:
      print("Valores nao aceitos")
  else:
    print("Valores nao aceitos")

else:
  print("Valores nao aceitos")