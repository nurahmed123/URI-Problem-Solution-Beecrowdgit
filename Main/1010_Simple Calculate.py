product_list_one = input().split(" ")
product_list_two = input().split(" ")

print("VALOR A PAGAR: R$ %.2f" %(int(float(product_list_one[1])) * float(product_list_one[2]) + int(float(product_list_two[1])) * float(product_list_two[2])))