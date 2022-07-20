area_value = input().split(" ")

triangle = float(area_value[0]) * float(area_value[2]) /2
circle = 3.14159 * float(area_value[2]) ** 2
trapezium = (float(area_value[0]) + float(area_value[1])) / 2 * float(area_value[2])
square = float(area_value[1]) ** 2
rectangle = float(area_value[0]) * float(area_value[1])


print("TRIANGULO: %.3f" % triangle)
print("CIRCULO: %.3f" % circle)
print("TRAPEZIO: %.3f" % trapezium)
print("QUADRADO: %.3f" % square)
print("RETANGULO: %.3f" % rectangle)
