# design a stack implmenting push, pop, min (retun min element) all operating in O(1) time.
# Hints:#27, #59, #78

from LinkedList import LinkedList
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.min = None

	def add(self, value):
		self.next = Node(value)
		if not self.min:
			self.min = value
		else:
			if self.min > value:
				self.next.min = value


class StackMin:
	def __init__(self):
		self.items = []
		self.min_item
		self.next_item

    def isEmpty(self):
        return self.items == []

	def push(self, item):
		self.items.append(item)
		if self.min_item:
			if self.next_min:
				if item < self.next_item and item > self.min_item:
					self.next_min = item
			else:
				if item < self.min_item:
					self.next_min = self.min_item
					self.min_item = item
		if isEmpty(self) or self.min_item > item:
			self.min_item = item

	def min(self):
    
    def peek(self):
        return self.items[len(self.items)-1]

	def pop(self):
		popped = self.items.pop()
		if popped == min_item:
			min_item = next_item
			next_item = None # I should keep them in a sorted list.
		return popped


	def min(self):
		# built in min function is O(N)
		# sort the stack? Doesn't make sense
		# keep track of the values as added makes sense but
		# I wouldn't be able to initialize on multiple values

		return min(items)
		

class StackMin2:
	def __init__(self):
		self.items = []
		self.mins = []

    def isEmpty(self):
        return self.items == []

	def push(self, item):
		self.items.append(item)
		if self.mins == []:
			self.mins.append(item)
		else:
			if self.mins[len(self.mins)-1] > item:
				self.mins.append(item)

    def peek(self):
        return self.items[len(self.items)-1]

	def pop(self):
		popped = self.items.pop()
		if popped == min(self):
			self.mins.pop()			
		return popped


	def min(self):
		return self.mins[len(self.mins)-1]
