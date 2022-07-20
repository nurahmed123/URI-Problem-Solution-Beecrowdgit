import math
a, b, c = list(map(float, input().split()))

formula = pow(b, 2) - 4*a*c

if(a == 0 or formula < 0):
    print("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(formula)) / (2 * a)
    x2 = (-b - math.sqrt(formula)) / (2 * a)

    print("R1 = %.5f" % (x1))
    print("R2 = %.5f" % (x2))
