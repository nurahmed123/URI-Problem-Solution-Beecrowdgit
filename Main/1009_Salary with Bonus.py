user_name  = input("")
user_salary = float(input())
user_extra_sale = float(input())

user_total_salary = user_salary + (user_extra_sale * 15/100)
print("TOTAL = R$ %.2f" %(user_total_salary))