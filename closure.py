# closures are value saving functions or functions which saves values and uses it later

def closure(outer):
    def inner(message="something"):
        print message,  outer, "value"
    return inner


clouse = closure("hi")
print clouse("hello")



def my_closure(number):
	def wrapper(a, b):
		return number + a * b
	return wrapper

my = my_closure(10)
print my(5,5)


def new_closure(number):
	def wrapper(a, b):
		result = a*b + number
		result += 20
		return result
	return wrapper


a = new_closure(20)
print a(5,5)


def outer():
	def inner(a, b):
		print a+b
		return None
	return inner

inner = outer()
inner(10, 20)