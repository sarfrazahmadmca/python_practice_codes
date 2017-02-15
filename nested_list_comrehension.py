# nested list comprehension
l1 = [i*j*k for i in range(5) for j in range(5) for k in range(5)]

# iterative version of nested list comprehansion

l2 = list()
for  i in range(5):
	for j in range(5):
		for k in range(5):
			l2.append(i*j*k)
print l1, l2
print l2 == l1