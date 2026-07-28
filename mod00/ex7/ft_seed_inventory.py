def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	capitalized = seed_type.capitalize()
	if unit == "packets":
		print("%s seeds: %d %s available" % (capitalized, quantity, unit))
	elif unit == "grams":
		print("%s seeds: %d %s total" % (capitalized, quantity, unit))
	elif unit == "area":
		print("%s seeds: covers %d square meters" % (capitalized, quantity))
	else:
		print("Unknown unit type")