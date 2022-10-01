from BinarySearchTreeNode import *

# ---------------------------------- Binary Search Tree -------------------------------
class BinarySearchTree:
    """
    | *Binary Search Tree Data Structure*
    | BST is a Binary Tree Data Structure in which -

    - Left Subtree of each Node stores Nodes with values *lesser* than the Node
    - Right Subtree of each Node stores Nodes with values *greater* than the Node
    - Left and Right Subtree each must also be a *Binary Search Tree*

    :param root: Root Node of BST, starting from which the Tree originates
    :type root: BSTNode

    | Available functions on a Binary Search Tree object are -
        
    - ``insert``  - Insert a new Node
    - ``traverse`` - Print the BST by traversing it in a given Order
    - ``height`` - Get height of subtree rooted at a given Node

    """
    
    def __init__(self):
        """
        Constructor to initialize a new BST, initializes ``root`` to `None`

        :Example:
            >>> bst = BinarySearchTree()
            >>> print(bst.root)
            None
        """
        self.root = None
    
    def insert(self, val):
        """
        Insert a New Node in BST with a given Value

        :param val: Value to be stored in New Node
        :type val: int

        :Example:
            >>> bst = BinarySearchTree()
            >>> bst.insert(20)
            >>> bst.insert(25)
            >>> bst.insert(50)
            >>> print(bst.root)
            20
        """
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info: # move to left sub-tree
                    if current.left:
                        current = current.left # root moved
                    else:
                        current.left = BSTNode(val) # left init
                        break
                elif val > current.info: # move to right sub-tree
                    if current.right:
                        current = current.right # root moved
                    else:
                        current.right = BSTNode(val) # right init
                        break
                else:
                    break # value exists
    
    def traverse(self, order):
        """
        Print the values stored in BST in a given Traversal Order

        :param order: Order of Traversal of Tree
        :type order: str

        | The Order of Traversal can be -
        
        - ``PRE``  : Current Node, left, right
        - ``IN``   : left, Current Node, right
        - ``POST`` : left, right, Current Node

        :Example:
            >>> bst = BinarySearchTree()
            >>> bst.insert(20)
            >>> bst.insert(25)
            >>> bst.insert(50)
            >>> bst.traverse("PRE")
            20 25 50 
        """
        def preOrder(root):
            print(root.info, end = ' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)
        def inOrder(root):
            if root.left != None:
                inOrder(root.left)
            print(root.info, end = ' ')
            if root.right != None:
                inOrder(root.right)
        def postOrder(root):
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end = ' ')
        if order == 'PRE':
            preOrder(self.root)
        elif order == 'IN':
            inOrder(self.root)
        elif order == 'POST':
            postOrder(self.root)
    
    def height(self, root):
        """
        | Function to get the Height of subtree rooted at a given Node.
        | Height here is defined as the longest distance of a Node to a leaf.

        :param root: Node whose height is to be found
        :type root: BSTNode
        :return: Height of the given Node
        :rtype: int

        :Example:
            >>> bst = BinarySearchTree()
            >>> bst.insert(20)
            >>> bst.insert(25)
            >>> bst.insert(50)
            >>> print(bst.height(bst.root))
            2
        """
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left),self.height(root.right))