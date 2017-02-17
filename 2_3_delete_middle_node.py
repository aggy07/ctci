from LinkedList import LinkedList

def delete_middle_node(middle):
    # Implement an algorithm to delete a middle node from a singly linket list, given access to only that node.
    # hint 72
    if not middle or not middle.next:
        return False
    
    middle.value = middle.next.value
    middle.next = middle.next.next
    
    return True


if __name__ == '__main__':

    ll = LinkedList()
    ll.add_multiple(['a', 'b'])
    middle_node = ll.add('c')
    ll.add_multiple(['d', 'e', 'f'])

    print(ll)
    delete_middle_node(middle_node)
    print(ll)