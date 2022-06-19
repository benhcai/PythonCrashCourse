foods = ['pi', 'za', 'and', 'is', ['ralph', 'reward']]
new_foods = foods[:]
print(foods)
new_foods[0] = 'new one'
new_foods[-1][0] = "zuccini"
# Shallow copy so the second level array is a reference
print(foods)
print(new_foods)

uppers = [val.upper() if type(val) == str else val for val in foods]
print(uppers)

flavors = ['red', 'blue', 'green', 'white']
colors = flavors
print(flavors)
colors[0] = 'teal'
print(flavors)
print(colors)
