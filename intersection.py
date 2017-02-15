def intersection(s1, s2):
	s3 = []
	for i in s1:
		if i in s2:
			s3.append(i)
	return s3

print intersection([1,2,3,4,5,6,7,8,9], [5,6,3,2])
