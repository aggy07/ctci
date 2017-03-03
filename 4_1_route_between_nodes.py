# find out if there is a route between two nodes of a directed graph.
# Hint 127

from Graph import Graph, Vertex

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue() #TODO make sure my queue implmentation matches pswads
    vertQueue.enqueue(start) # add
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue() # remove
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currenteVert)
                vertQueue.enqueue(nbr)
            currentVert.setColor('black')
            