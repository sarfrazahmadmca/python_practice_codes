def check_ap(alist):
	alist = sorted(alist)
	diff = alist[1] - alist[0]
	length = len(alist) - 1
	while length:
		if not alist[length] - alist[length-1] == diff:
			print "can't form AP"
			return
		length -= 1
	print "can form AP"


check_ap(range(1,10))
check_ap([1,3,5,7,9, 13])
