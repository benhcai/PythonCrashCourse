alien_0 = {'color': 'green', 'age': 10}
alien_1 = {'color': 'blue', 'age': 15}
alien_2 = {'color': 'red', 'age': 20}

aliens = []

for _n in range(30):
    new_alien = alien_0.copy()
    aliens.append(new_alien)

aliens[0]['color'] = 'purple'

for alien in aliens[:5]:
    print(alien)
