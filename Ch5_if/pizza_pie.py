requested_toppings = ['shrooms', 'cheese', 'chicken', 'pepperoni', 'egg']

if 'shrooms' in requested_toppings:
    print('Has shrooms')
if 'cheese' in requested_toppings:
    print('Has cheese')
if 'bacon' in requested_toppings:
    print('Has bacon')
else:
    print('No bacon')

print('-----')

for topping in requested_toppings:
    if topping == 'chicken':
        print('no chicken')
    else:
        print(topping)
