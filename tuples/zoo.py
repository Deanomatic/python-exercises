zoo = ("Fox", "Mammoth", "Lizard")

for animal in zoo:
	if(animal == "Fox"):
		print(animal)

(lizard, fox, mammoth) = zoo
print(zoo.index("Fox"), zoo)

zoo_list = list(zoo)

more_animals = ["Python", "Monkey", "Bear"]
zoo_list.extend(more_animals)

better_than_aaron_zoo = tuple(zoo_list)

print(better_than_aaron_zoo)