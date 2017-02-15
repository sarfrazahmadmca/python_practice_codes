def bubble_sort(li):
	n = len(li)
	for i in range(n):
		"""In each step the largest number will reach to the end or its correct position, so ineer loop will be n-1-i"""
		for j in range(0, n-i-1):	
			if li[j] >  li[j + 1]:
				li[j], li[j+1] = li[j+1] , li[j]
	return li

li = [3,1,2,7,4,6,5,0, 9, 1]
print bubble_sort(li)

