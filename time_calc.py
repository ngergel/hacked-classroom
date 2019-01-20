def time_compare(x, start, end):
	x, start, end = list(map(int, x.split(':'))), list(map(int, start.split(':'))), list(map(int, end.split(':')))

	if x[0] >= start[0] and x[0] < end[0]:
		return True
	if x[0] == end[0] and x[1] >= start[1] and x[1] < end[1]:
		return True
	else:
		return False