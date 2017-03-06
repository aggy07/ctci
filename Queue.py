# Implement a queue using two stacks
# Hints #98 #114

import unittest

class Queue():
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, value):
        qn = QueueNode(value)
        if self.last is not None:
            self.last.next = qn
        self.last = qn

        if self.first is None:
            self.first = self.last

    def dequeue(self):
        if self.first is None:
            return False
        
        value = self.first.value
        
        self.first = self.first.next
        
        if self.first is None:
            self.last = None
        
        return value

    def peek(self):
        if self.first is None:
            return False
        return self.first.value

    def size(self):
        result = 0
        node = self.first
        while node:
            result += 1
            node = node.next
        return result


    def is_empty(self):
        return self.first == None


class QueueNode():
    def __init__(self, value):
        self.value = value
        self.next = None



class Tests(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        for i in range(35):
            q.enqueue(i)
        remove_list = []
        for _ in range(35):
            remove_list.append(q.dequeue())
        self.assertEqual(remove_list, list(range(35)))

if __name__ == '__main__':
    unittest.main()



