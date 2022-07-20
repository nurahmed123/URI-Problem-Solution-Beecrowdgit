amount = float(input())

print("NOTAS:")
note_list = [100, 50, 20, 10, 5, 2]
coin_list = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]

for notes in note_list:
  print(f"{int(amount / notes)} nota(s) de R$ {notes}.00")
  amount = float(f"{amount % notes:.2f}")

print("MOEDAS:")
for coin in coin_list:
  print(f"{int(amount / coin)} moeda(s) de R$ {coin:.2f}")
  amount = float(f"{amount % coin:.2f}")