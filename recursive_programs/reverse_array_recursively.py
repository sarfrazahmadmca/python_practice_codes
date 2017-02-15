def array_elements_recursive(alist):
	if not alist:
		return
	print alist.pop(-1)
	array_elements_recursive(alist)

array_elements_recursive(range(10))
