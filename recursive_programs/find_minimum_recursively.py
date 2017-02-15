def find_minimum(alist):
	if len(alist) == 1:
		return alist[0]
	return min(alist[0], find_minimum(alist[1:]))

print find_minimum([32,234,23,12,31,213,123,24,34,34,534,5,234,13,12,123,432,35,34,34,3])
