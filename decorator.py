# a decorator to add the square of values passed to it
def square_decorator(func):
	def inner(a, b):
		a = a*a 
		b = b*b
		return func(a, b)
	return inner


@square_decorator
def square_sum(a, b):
	return a + b

print square_sum(5, 3)



# A decorator to check if the index is not more than the length of a list.

def check_index_decorator(func):
	def inner(alist, index):
		if index > len(alist)-1:
			raise IndexError("Index is  out of range")
		return func(alist, index)
	return inner

@check_index_decorator
def get_element(alist, index):
	return alist[index]


print get_element(range(10), 5)
print get_element(range(10), 11)
