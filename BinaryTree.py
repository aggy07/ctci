# https://interactivepython.org/runestone/static/pythonds/Trees/NodesandReferences.html

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        retrun self.leftChild

    def getRootVal(self):
        return self.key
