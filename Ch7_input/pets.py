pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
put_down = []

# while might be better than for if you are modifying the list
while 'dog' in pets:
    el_index = pets.index('dog')
    el = pets.pop(el_index)
    put_down.append(el)

print(pets)
print(put_down)
