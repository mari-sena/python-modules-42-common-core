def ft_water_reminder():
	days = int(input())
	print("Days since last watering: %d" % days)
	if days > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")