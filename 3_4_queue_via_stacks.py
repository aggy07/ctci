# Implement a queue using two stacks
# Hints #98 #114

import unittest
from Stack import Stack

class Queue():
    def __init__(self):
        self.stack_newest = Stack()
        self.stack_oldest = Stack()

    def size(self):
        return self.stack_newest.size() + self.stack_oldest.size()

    def add(self, value):
        self.stack_newest.push(value)

    def shift_stacks(self):
        if self.stack_oldest.is_empty():
            while not self.stack_newest.is_empty():
                self.stack_oldest.push(self.stack_newest.pop())

    def peek(self):
        self.shift_stacks()
        return self.stack_oldest.peek()
    
    def remove(self):
        self.shift_stacks()
        return self.stack_oldest.pop()




class Tests(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        for i in range(35):
            q.add(i)
        remove_list = []
        for _ in range(35):
            remove_list.append(q.remove())
        self.assertEqual(remove_list, list(range(35)))

if __name__ == '__main__':
    unittest.main()



