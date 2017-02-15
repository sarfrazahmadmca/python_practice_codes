class Queue(object):

	def __init__(self):
		self.data = []
		super(Queue, self).__init__()

	def enqueue(self, value):
		self.data.append(value)
		return self.data

	def dequeue(self):
		if self.data:
			return self.data.pop()
		return None

	def is_empty(self):
		if not len(self.data):
			return True
		return False

	def rear(self):
		if not self.is_empty():
			return self.data[-1]
		return False

	def front(self):
		if not self.is_empty():
			return self.data[0]
		return False



q = Queue()
print q.enqueue(10)
print q.enqueue(20)
print q.dequeue()
print q.dequeue()
print q.data