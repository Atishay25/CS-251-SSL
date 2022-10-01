from  SinglyLinkedListNode import *

# ------------------------------ Singly Linked List -------------------------------

class SinglyLinkedList:
    """
    | *Singly Linked List Data Structure*
    | It is the simplest type of linked list in which every node contains 
      some data and a pointer to the next node of the same data type.

    :param head: Reference to first Node of Linked List
    :param tail: Reference to last Node of Linked List
    :type head: SinglyLinkedListNode
    :type tail: SinglyLinkedListNode

    | Available functions on a Singly Linked List object are -

    - ``insert`` - Insert a new Node
    - ``find`` - Find a particular Node
    - ``deleteVal`` - Delete a particular Node
    - ``printer`` - Print the Linked List
    - ``reverse`` - Reverse the order of elements in Linked List
    """
    
    def __init__(self):
        """
        | Constructor for Singly Linked List
        | Initializes ``head`` and ``tail`` to `None`

        :Example:
            >>> linkedList = SinglyLinkedList()
            >>> linkedList.printer()
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
            >>> linkedList = SinglyLinkedList()
            >>> linkedList.printer()
            []
            >>> linkedList.insert(25)
            >>> linkedList.printer()
            [25]
            >>> linkedList.insert(15)
            >>> linkedList.printer()
            [25, 15]

        """
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    def find(self, data):
        """
        Find Previous Node of a Node with a given data
        
        :param data: value of data to be found
        :type data: int
        :param prev: Previous Node
        :type prev: SinglyLinkedListNode
        :return: Previous Node of the Node with given data (if found), else returns `None`
        :rtype: int

        :Example:
            >>> linkedList = SinglyLinkedList()
            >>> linkedList.insert(25)
            >>> linkedList.insert(15)
            >>> linkedList.insert(12)
            >>> linkedList.printer()
            [25, 15, 12]
            >>> prevNode = linkedList.find(12)
            >>> print(prevNode.data)
            15
        """
        head = self.head
        prev = None
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev
    
    def deleteVal(self, data):
        """
        Delete the Node with given data

        :param data: value stored in the Node which is to be deleted
        :type data: int
        :return: `True`, if desired `Node` is deleted
        :return: `False`, if Node to be deleted is None already
        :rtype: bool

        :Example:
            >>> linkedList = SinglyLinkedList()
            >>> linkedList.insert(10)
            >>> linkedList.insert(20)
            >>> linkedList.insert(30)
            >>> linkedList.printer()
            [10, 20, 30]
            >>> delNode = linkedList.deleteVal(20)
            >>> print(delNode)
            True
            >>> linkedList.printer()
            [10, 30]
            >>> delNode2 = linkedList.deleteVal(50)
            >>> print(delNode2)
            False
            >>> linkedList.printer()
            [10, 30]
        """
        prevPos = self.find(data)
        if prevPos.next == None:
            return False
        prevPos.next = prevPos.next.next
        return True
    
    def printer(self, sep = ', '):
        """
        Function to print the Linked List with a given separation
        between the Data stored in each Node

        :param sep: Separation to be used between Data of each node while printing the linked list
        :type sep: str

        :Example:
            >>> linkedList = SinglyLinkedList()
            >>> linkedList.insert(25)
            >>> linkedList.insert(15)
            >>> linkedList.insert(12)
            >>> linkedList.printer()
            [25, 15, 12]
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
            >>> linkedList = SinglyLinkedList()
            >>> linkedList.insert(10)
            >>> linkedList.insert(20)
            >>> linkedList.insert(30)
            >>> linkedList.printer()
            [10, 20, 30]
            >>> linkedList.reverse()
            >>> linkedList.printer()
            [30, 20, 10]
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev
