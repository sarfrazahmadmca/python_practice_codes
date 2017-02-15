# Return index, value and a string if value found else return -1
def binary_search(alist, value, left, right):

	if right >= left:
		mid = left + (right - left) / 2
		if alist[mid] == value:
			return mid, alist[mid], "found"

		if value < alist[mid]:
			right = mid -1

		if value > alist[mid]:
			left = mid + 1

		return binary_search(alist, value, left, right)
	else:
		return - 1

li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print binary_search(li, 23, 0, len(li)-1)
print binary_search(li, 11, 0, len(li)-1)
