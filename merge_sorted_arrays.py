def merge(arr1, arr2):
	if not len(arr1) and not len(arr2):
		return []

	if arr1 and not arr2:
		return arr1
	if arr2 and not arr1:
		return arr2

	sorted_array = list()
	while len(arr1) and len(arr2):
		if arr1[0] < arr2[0]:
			elem = arr1.pop(0)
			sorted_array.append(elem)
		else:
			elem = arr2.pop(0)
			sorted_array.append(elem)
	if len(arr1):
		sorted_array.extend(arr1)
	if len(arr2):
		sorted_array.extend(arr2)
	return sorted_array

print merge([3,4, 5, 9], [1,2, 6, 8])