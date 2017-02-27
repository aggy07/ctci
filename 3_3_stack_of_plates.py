# Implement data structure for setofstacks that creates a new stack once the previous is full.
# Push and pop should work the same as for a single stack.  
# Impleent pop_at(index) to pop on specific sub-stack.
# Hints:#64, #87

class MultiStack:
    
    def __init__(self, stacksize):
        self.numstacks = 1
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def Push(self, item):
        stacknum=self.numstacks-1
        if self.IsFull(stacknum): # always check the top stack
            self.numstacks += 1 # add stack to the top
            self.array.append(item)
            for i in range(self.stacksize-1):
                self.array.append(0) # append additional empty elements less the already added zeroth element
            self.sizes.append(1)
        else:
            self.sizes[stacknum] += 1
            self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self):
        stacknum=self.numstacks-1
        if self.IsEmpty(stacknum):
            self.numstacks -= 1
            for i in range(self.stacksize-1):
                self.array.pop() # pop one stack's worth of [0] elements
            self.sizes.pop()
            value = self.array[self.IndexOfTop(stacknum)-1]
            self.array[self.IndexOfTop(stacknum)-1] = 0 # should get top element of next stack
        else:
            value = self.array[self.IndexOfTop(stacknum)]
            self.array[self.IndexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
        return value

    def Peek(self):
        stacknum=self.numstacks-1
        print('Peek stacknum', stacknum)
        print('Peek array', self.array)
        if self.IsEmpty(stacknum):
            self.array[self.IndexOfTop(stacknum)-1]
        return self.array[self.IndexOfTop(stacknum)]

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IndexOfTop(self, stacknum):
        print('IofT stacknum', stacknum)
        print('IofT stacksize', self.stacksize)
        offset = stacknum * self.stacksize
        print('IofT offset', offset)
        print('IofT stack {} size {}'.format(stacknum, self.sizes[stacknum]))
        return offset + self.sizes[stacknum] - 1 

if __name__ == '__main__':

    newstack = MultiStack(2)
    print(newstack.IsEmpty(0))
    newstack.Push(3)
    print(newstack.Peek())
    print(newstack.IsEmpty(0))
    newstack.Push(2)
    print(newstack.Peek())
    newstack.Push(4)
    print(newstack.Peek())
    newstack.Push(5)
    print(newstack.Peek())
    newstack.Push(6)
    print('Peek newly added 6 on stack 2: ', newstack.Peek())
    print('Pop 6', newstack.Pop())
    print('Peek top of stack 1: ',newstack.Peek())
    print('Pop top of stack 1: ',newstack.Pop())
    print('Peek 0th of stack 1: ',newstack.Peek())
    print('Pop 0th of stack 1: ', newstack.Pop())
    print('Peek top of stack 0: ',newstack.Peek())
    print('Pop top of stack 0: ',newstack.Pop())
    print('Peek 0th of stack 0: ',newstack.Peek())

# Opportunities: the book solution uses a list of lists instead of the multistack implementation.  Same things need to happen but simpler to deal with.