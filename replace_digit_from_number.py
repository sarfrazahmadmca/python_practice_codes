def replace_number(number, value, replace_by):
	if number == 0:
		return 0
	digit = number % 10
	if digit == value:
		digit = replace_by
	return digit + 10 * replace_number(number/10, value, replace_by)


print 12120234212, replace_number(12120234212, 2, 5)
print 12129294292, replace_number(12129294292, 9, 3)


