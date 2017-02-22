from LinkedList import LinkedList

def is_intersection(ll_a, ll_b):
    ''' Determine if two (singly) linked lists intersect by reference and return intersecting
    node. 
    Hints:#20, #45, #55, #65, #76, #93, #111, #120, #129 '''
    if not ll_a and not ll_b:
        return None

    current_a = ll_a.head
    current_b = ll_b.head
    len_a = 0
    len_b = 0
    
    while current_a:
        if not current_a.next:
            tail_a = current_a
        current_a = current_a.next
        len_a += 1

    while current_b:
        if not current_b.next:
            tail_b = current_b
        current_b = current_b.next
        len_b += 1

    if tail_a is not tail_b:
        return None
        
    if len_a > len_b:
        diff = len_a - len_b
        longer = ll_a.head
        shorter = ll_b.head
    elif len_b > len_a:
        diff = len_b - len_a
        longer = ll_b.head
        shorter = ll_a.head
    else:
        diff = 0
        longer = ll_b.head
        shorter = ll_a.head

    for i in range(diff):
        longer = longer.next

    while longer is not shorter:
            longer = longer.next
            shorter = shorter.next
    return longer

def is_intersection2(ll1, ll2):
    if ll1.tail is not ll2.tail:
        return False

    shorter = ll1 if len(ll1) < len(ll2) else ll2
    longer = ll2 if len(ll1) < len(ll2) else ll1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for i in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node
    


if __name__ == '__main__':

    ll_a = LinkedList([1,2,3,4,5])
    ll_b = LinkedList([12,11,6,7,8])

    print(ll_a)
    print(ll_b)
    print()
    node = ll_a.head.next.next
    node.next = ll_b.head.next 
    ll_b.head.next = node
    ll_a.tail = ll_b.tail
    print(ll_a)
    print(ll_b)
    print()
    print(is_intersection(ll_a, ll_b))
    print(is_intersection2(ll_a, ll_b))

# Opportunities: My example led me to the hidden assumption that the lists would be in sync.  So I failed to compare each element of one list to all elements of the other.  Reading the hints showed that if I had been comparing the tail nodes that would have been fine.
# Opportunities: modularize, cleanup the nasty conditionals with ternary syntax, correct the ll.tail issue

