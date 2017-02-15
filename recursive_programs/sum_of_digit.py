def digits_sum(n):
	if not n:
		return 0
	digit = n % 10 
	n = n / 10
	return digit + digits_sum(n)

print digits_sum(123)
print digits_sum(12)
print digits_sum(155)