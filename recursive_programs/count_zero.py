def count_zero(alist):
	if not alist:
		return 0
	number = alist.pop(0)
	return 1 + count_zero(alist) if number is 0 else 0 + count_zero(alist)


print count_zero([1,0,2,1,0,9,0,9,0])
print count_zero([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
