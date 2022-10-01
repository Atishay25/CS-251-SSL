# ------------------------------ Doubly Linked List Node -----------------------------


class DoublyLinkedListNode:
    """
    | *Node of a Doubly Linked List*
    | A Double Linked List Node stores an additional pointer as compared to a 
      Singly Linked List Node, mainly to point to Previous Node as well
    | Each Node in a Singly Linked List stores -
      
    1. **Data** value (can be of any data type like int, str, float etc)
    2. **Pointer** (or reference) to its next Node
    3. **Pointer** (or reference) to its previous Node

    :param data: Value to be stored in a Node
    :type data: int
    :param next: Pointer to next Node
    :type next: SinglyLinkedListNode
    :param prev: Pointer to previous Node
    :type prev: DoublyLinkedListNode

    """
    
    def __init__(self, data):
        """
        | Constructor to initialize a new Doubly Linked List Node object
        | It initializes ``next`` and ``prev`` to `None` and ``data`` to given data value

        :param data: Value to be stored in Node 
        :type data: int

        :Example: 
            >>> dlNode = DoublyLinkedListNode(45)
            >>> print(dlNode.data)
            45

        """
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        """
        Converter to return value of data stored, converted into string data type

        :return: Data stored in Node in string data type
        :rtype: str

        :Example:
            >>> Node = DoublyLinkedListNode(10)
            >>> dataStr = Node.__str__()
            >>> print(dataStr)
            10
            >>> print(type(dataStr))
            <class 'str'>

        """
        return str(self.data)