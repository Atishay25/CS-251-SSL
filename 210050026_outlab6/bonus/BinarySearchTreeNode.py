# -------------------------- Binary Search Tree Node ------------------------------

class BSTNode:
    """
    | *Node of a Binary Search Tree*

    :param info: Value stored at a Node
    :param left: Reference to left Node
    :param right: Reference to right Node
    :param level: Height of the Node
    :type info: int
    :type left: BSTNode
    :type right: BSTNode
    :type level: int

    """
    
    def __init__(self, info):
        """
        Constructor to initialize a new BSTNode object

        :param info: Value to be stored in Node
        :type info: int

        :Example:
            >>> bstNode = BSTNode(25)
            >>> print(bstNode.info)
            25

        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        """
        Converter to return value stored , but converted into string data type

        :return: Data stored in Node in string data type
        :rtype: str
        
        :Example:
            >>> bstNode = BSTNode(25)
            >>> info_str = bstNode.__str__()
            >>> print(info_str)
            25
            >>> print(type(info_str))
            <class 'str'>
        """
        return str(self.info)