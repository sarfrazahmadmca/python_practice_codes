# an example of parameterized decorator

def parameterized_decorator(a, b):
	def main_decorator(func):
		def wrapper(c, d):
			result =  func(a, b)
			result2 = func(c,d)
			return result+result2
		return wrapper
	return main_decorator


@parameterized_decorator(10, 30)
def sub(a=0, b=0):
	return b - a

print sub(10, 20)