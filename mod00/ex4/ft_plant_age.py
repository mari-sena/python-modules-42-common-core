def ft_plant_age():
    plant_days = int(input())
    print("Enter plant age in days: %d" % plant_days)
    if plant_days > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
