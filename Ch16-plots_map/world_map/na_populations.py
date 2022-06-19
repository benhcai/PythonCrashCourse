import pygal

wm = pygal.maps.world.World()
wm.tltle = "Populations of Countries in North America:"
wm.add("North America", {'ca': 30000000, 'us': 300000000, 'mx': 100000000})
wm.render_to_file('na_populations.svg')
