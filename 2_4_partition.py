from LinkedList import LinkedList

def partition(ll, p):
    # partition a linked list around a value x such that all nodes less than x come before all nodes greater than or equal to x. x can appear anywhere on the proper side.
    # Hint 3, 24
    lt = LinkedList()
    gt = LinkedList()

    for node in ll:
        if node.value < p:
            lt.add(node)
        else:
            gt.add(node)
    lt.tail.next = gt.head
    
    return lt

def partition2(ll, p):
    current = ll.tail = ll.head

    while current:
        nextNode = current.next
        current.next = None
        if current.value < p:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None

    
        
    
    
            


    
    return ll



if __name__ == '__main__':

    ll = LinkedList()
    ll.add_multiple([3, 5, 8, 5, 10, 2, 1])

    print(ll)
    ll = partition(ll, 5)
    print(ll)

    ll = LinkedList()
    ll.add_multiple([3, 5, 8, 5, 10, 2, 1])

    print(ll)
    ll = partition2(ll, 5)
    print(ll)
