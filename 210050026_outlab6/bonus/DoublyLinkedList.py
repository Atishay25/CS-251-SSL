from  DoublyLinkedListNode import *

# ------------------------------ Doubly Linked List -----------------------------

class DoublyLinkedList:
    """
    | *Doubly Linked List Data Structure*
    | A Doubly Linked List (DLL) contains an extra pointer, typically 
      called the previous pointer, together with the next pointer and 
      data which are there in the singly linked list.

    :param head: Head/First Node of the Linked List
    :param tail: Tail/Last Node of the Linked List
    :type head: DoublyLinkedListNode
    :type tail: DoublyLinkedListNode

    | Available functions on a Doubly Linked List object are -
        
    - ``insert``  - Insert a new Node
    - ``printer`` - Print the Linked List
    - ``reverse`` - Reverse the order of elements in Linked List

    """
    
    def __init__(self):
        """
        | Constructor for Singly Linked List
        | Initializes ``head`` and ``tail`` to `None`

        :Example:
            >>> dlList = DoublyLinkedList()
            >>> dlList.printer()
            []

        """
        self.head = None
        self.tail = None
    
    def insert(self, data):
        """
        Insert a new Node into the Linked List with a particular data stored in it. 

        :param data: value to be stored in new Node inserted
        :type data: int

        :Example:
            >>> dlList = DoublyLinkedList()
            >>> dlList.insert(25)
            >>> dlList.insert(50)
            >>> dlList.insert(75)
            >>> dlList.printer()
            [25, 50, 75]

        """
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep = ', '):
        """
        Function to print the Linked List with a given separation
        between the Data stored in each Node

        :param sep: Separation to be used between Datam of each node while printing the linked list
        :type sep: str

        :Example:
            >>> dlList = DoublyLinkedList()
            >>> dlList.insert(25)
            >>> dlList.insert(50)
            >>> dlList.printer()
            [25, 50]

        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """
        Reverse the Order of Elements in the Linked List

        :Example:
            >>> dlList = DoublyLinkedList()
            >>> dlList.insert(25)
            >>> dlList.insert(50)
            >>> dlList.insert(75)
            >>> dlList.printer()
            [25, 50, 75]
            >>> dlList.reverse()
            >>> dlList.printer()
            [75, 50, 25]

        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev