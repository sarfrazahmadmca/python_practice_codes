# Linear search using iterating over elements
def search(lst, value):
	for i in lst:
		if i == value:
			return True
	return False

print search([1, 2, 3, 4, 5, 6], 7)
print search([1, 2, 3, 4, 5, 6], 5)


# Linear search using indexing

def linear_search(alist, value):
	for i in range(len(alist)):
		if alist[i] == value:
			return True
	return False

print linear_search([1, 2, 3, 4, 5, 6], 7)
print linear_search([1, 2, 3, 4, 5, 6], 3)


# Linear Search using recursive function
def linear_search_recursively(alist, value):
	if not alist:
		return False
	element = alist.pop(0)
	if element == value:
		return True
	return linear_search_recursively(alist, value)

print linear_search_recursively([1, 2, 3, 4, 5, 6], 7)
print linear_search_recursively([1, 2, 3, 4, 5, 6], 6)
