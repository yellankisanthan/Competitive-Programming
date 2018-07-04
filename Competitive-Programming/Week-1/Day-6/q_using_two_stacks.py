class Node:
	def __init__(self,data,nextNode=None):
		self.data = data
		self.nextNode = nextNode

	def getData(self):
		return self.data

	def setData(self,val):
		self.data = val

	def getNextNode(self):
		return self.nextNode

	def setNextNode(self,val):
		self.nextNode = val
	
class Stack(object):
	def __init__(self,head = None):
		self.head = head
		self.size = 0

	def push(self,data):
		newNode = Node(data,self.head)
		self.head = newNode
		self.size += 1
		return True
	
	def pop(self):
		try:
			x = self.head.data
			self.head = self.head.nextNode
			self.size -= 1
			return x
		except:
			return False
	
	def getSize(self):
		return self.size

class QueueTwoStacks(object):

	# Implement the enqueue and dequeue methods
	def __init__(self):
		self.a = Stack()
		self.b = Stack()

	def enqueue(self, item):
		while self.a.head is not None:
			self.b.push(self.a.pop())
		self.a.push(item)
		while self.b.head is not None:
			self.a.push(self.b.pop())

	def dequeue(self):
		if self.a.getSize() == 0:
			raise ValueError()
		
		return self.a.pop()




# Tests

queue = QueueTwoStacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

actual = queue.dequeue()
expected = 1
print(actual == expected)

actual = queue.dequeue()
expected = 2
print(actual == expected)

queue.enqueue(4)

actual = queue.dequeue()
expected = 3
print(actual == expected)

actual = queue.dequeue()
expected = 4
print(actual == expected)