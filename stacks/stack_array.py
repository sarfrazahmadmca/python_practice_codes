class Stack(object):

	def __init__(self):
		self.data = []

	def push(self, value):
		self.data.append(value)

	def pop(self):
		if self.is_empty():
			raise IndexError("Index out range")
		return self.data.pop()

	def peek(self):
		if self.is_empty():
			raise IndexError("Stack is empty")
		return self.data[-1]

	def is_empty(self):
		if not len(self.data):
			return True
		return False

	def size(object):
		return len(self.data)

	def clear(self):
		del self.data[:]

	def reverse(self, stack):

		if not stack:
			return
		element = stack[-1]
		self.reverse(stack[:-1])
		print element

	def traverse(self, stack):
		if not stack:
			return
		print stack[-1]
		self.traverse(stack[:-1])
		



stack = Stack()
for i in range(0, 20, 3):
	stack.push(i)
stack.reverse(stack.data)
stack.traverse(stack.data)

print stack.data

print stack.pop()
print stack.peek()

print stack.pop()
print stack.peek()

print stack.pop()
print stack.peek()

print stack.pop()
print stack.peek()
print stack.data