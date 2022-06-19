age = 80

if age < 4:
    print("you get free admission")
    price = 0
elif age < 18:
    print('you get student fare')
    price = 5
elif age < 60:
    print('you get full fare')
    price = 10
else:
    print('you get senior citizen fare')
    price = 8 

print('Cost of admission for u is: $' + str(price))
