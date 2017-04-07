showroom = set()
showroom.add("Ford Mustang")
showroom.add("Shelby Cobra")
showroom.add("VW Bug")
showroom.add("Dodge Viper")
showroom.add("Dodge Viper")


showroom.update({"Plymouth Prowler", "Veyron"})

showroom.discard("Plymouth Prowler")


junkyard = set()
junkyard.add("Ford Mustang")
junkyard.add("VW Bug")
junkyard.add("Pontiac GTO")
junkyard.add("Ashton Martin")
junkyard.add("McLaren F1")

junk = junkyard.intersection(showroom)

print(junk)
print(showroom | junkyard)
