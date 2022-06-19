cars = ['bmw', 'audi', 'ferrari', 'toyota']

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car)

print('----end1----')

for car in cars:
    if car != "toyota":
        print(car)
