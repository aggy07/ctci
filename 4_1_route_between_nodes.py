# find out if there is a route between two nodes of a directed graph.
# Hint 127

from Graph import Graph, Vertex
from Queue import Queue
def bfs(g, start, finish):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue() #TODO make sure my queue implmentation matches pswads
    vertQueue.enqueue(start) # add
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue() # remove
        for nbr in currentVert.getConnections():
            if nbr == finish:
                return True
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
            currentVert.setColor('black')
    return False

if __name__ == '__main__':

    print("Create Graph:")
    g = Graph()
    for i in range(8):
        g.addVertex(i)
    g.vertList
    #g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    #g.addEdge(3,6,1)
    g.addEdge(6,7,1)
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

    start = g.getVertex(0)
    finish = g.getVertex(7)
    print('Is there a route from {} to {}? {}'.format(start.id, finish.id, bfs(g, start, finish)))