import pizza as p
from cook import cook_pizza
from send import send_pizza_away as send_pizza
from add_ingredients import *

p.make_pizza("cheese", "apple")
p.make_pizza("cherry", "tomato", "brocolli")

cook_pizza("Supremem Pizza")
cook_pizza("Surf and Turf")

send_pizza("steve")
send_pizza("jerr")

tomato()
cheese()
