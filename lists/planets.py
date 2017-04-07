solar_system = list()
solar_system = ["Mercury", "Mars"]
solar_system.append("Saturn")
solar_system.append("Jupiter")

more_planets = ["Neptune", "Pluto"]
solar_system.extend(more_planets)
solar_system.insert(1, "Earth")
solar_system.insert(2, "Venus")

spaceships = [('Cassini', 'Saturn'),
	("Slave I", "Venus"), 	
	("X Wing", "Jupiter")]

rocky_planets = solar_system[1: 3]

del solar_system[7]

for planet in solar_system:
    ships = list()
    for spaceship in spaceships:
        if(planet == spaceship[1]):
           ships.append(spaceship[0])

    print("Ships that have visited {}: {}".format(planet, str(ships)))
# print(rocky_planets)
# print(solar_system)