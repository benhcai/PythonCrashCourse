requested_toppings = ['mushrooms', 'cheese', 'chicken', 'bacon']
available_toppings = ['mushrooms', 'cheese', 'bacon']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping)
    else:
        print("Not available: " + requested_topping)
print("Pizza done!")
