def count_days(current_day, days):
	if current_day > days:
		return ;
	print("Day %d" % current_day)
	count_days(current_day + 1, days)

def ft_count_harvest_recursive():
	days = int(input())
	print("Days until harvest: %d" % days)
	count_days(1, days)
	print("Harvest time!")

