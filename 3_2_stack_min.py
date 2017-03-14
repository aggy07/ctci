# design a stack implmenting push, pop, min (retun min element) all operating in O(1) time.
# Hints:#27, #59, #78

class StackMin:
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
