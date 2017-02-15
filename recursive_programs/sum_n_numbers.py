def sum_n_numbers(n):
	if n ==1:
		return 1
	return n+ sum_n_numbers(n-1)



print sum_n_numbers(1)
print sum_n_numbers(2)
print sum_n_numbers(3)
print sum_n_numbers(4)
print sum_n_numbers(5)
