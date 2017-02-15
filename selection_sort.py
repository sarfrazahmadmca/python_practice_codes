def selection_sort(li):

	if not li:
		return li
	if len(li) == 1:
		return li

	for i in range(0, len(li)):
		for j in range(i+1, len(li)):
			if li[i] > li[j]:
				temp = li[i]
				li[i] = li[j]
				li[j] = temp

	return li


li = [3,1,2,7,4,6,5,0, 9, 1]
print selection_sort(li)
