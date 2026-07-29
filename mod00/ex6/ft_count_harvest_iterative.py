def ft_count_harvest_iterative():
    days = int(input())
    print("Days until harvest: %d" % days)
    for day in range(1, days + 1):
        print("Day %d" %day)
    print("Harvest time!")
