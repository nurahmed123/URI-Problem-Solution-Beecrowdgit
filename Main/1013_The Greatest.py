user_input = input().split(" ")
a, b, c = user_input

calculation = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
Result = (int(calculation) + int(c) + abs(int(calculation) - int(c)))/2

print("%d eh o maior" %Result)