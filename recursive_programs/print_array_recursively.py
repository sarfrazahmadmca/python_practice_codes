def array_elements(alist):
	if not alist:
		return
	print alist.pop(0)
	array_elements(alist)

array_elements([1,2,3,4,5,6,7,8,9,])
