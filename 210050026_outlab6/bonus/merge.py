from SinglyLinkedList import *

# ------------------------------- Merge Function ----------------------------------

def merge(list1, list2):
    """
    Function to Merge two Singly Linked Lists into one Singly Linked List

    :param list1: First Linked List to be merged
    :type list1: SinglyLinkedList
    :param list2: Second Linked List to be merged
    :type list2: SinglyLinkedList
    
    :return: Merged Linked List
    :rtype: SinglyLinkedList
    
    :Example:
        >>> list1 = SinglyLinkedList()
        >>> list1.insert(10)
        >>> list1.insert(20)
        >>> list2 = SinglyLinkedList()
        >>> list2.insert(150)
        >>> list2.insert(160)
        >>> list1.printer()
        [10, 20]
        >>> list2.printer()
        [150, 160]
        >>> merge_list = merge(list1,list2)
        >>> merge_list.printer()
        [10, 20, 150, 160]

    """
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged