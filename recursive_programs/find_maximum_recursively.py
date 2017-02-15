def maximum(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))

print maximum([32,234,23,12,31,213,123,24,34,34,534,5,234,13,12,123,432,35,34,34])

	
