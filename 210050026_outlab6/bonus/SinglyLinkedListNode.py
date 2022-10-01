# ------------------------------ Singly Linked List Node ------------------------------


class SinglyLinkedListNode:
    """
    | *Node of a Singly Linked List*
    | Each Node in a Singly Linked List stores -
      
    1. **Data** value (can be of any data type like int, str, float etc)
    2. **Pointer** (or reference) to its next Node

    :param data: Value to be stored in a Node
    :type data: int
    :param next: Reference to next Node
    :type next: SinglyLinkedListNode

    """
    
    def __init__(self, data):
        """
        | Constructor to initialize a new Singly Linked List Node object
        | Initializes a Node with given ``data`` stored in it and ``next`` Pointer as `None`

        :param data: Value to be stored in a Node
        :type data: int

        :Example:
            >>> Node = SinglyLinkedListNode(10)
            >>> print(Node.data)
            10
            >>> print(Node.next)
            None

        """
        self.data = data
        self.next = None
    
    def __str__(self):
        """
        Converter to return value of data stored, converted into string data type

        :return: Data stored in Node in string data type
        :rtype: str

        :Example:
            >>> Node = SinglyLinkedListNode(10)
            >>> dataStr = Node.__str__()
            >>> print(dataStr)
            10
            >>> print(type(dataStr))
            <class 'str'>

        """
        return str(self.data)