################################## Data Structures ################################


# ------------------------------- Singly Linked List -----------------------------


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
            >>> from DSA import SinglyLinkedListNode
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
            >>> from DSA import SinglyLinkedListNode
            >>> Node = SinglyLinkedListNode(10)
            >>> dataStr = Node.__str__()
            >>> print(dataStr)
            10
            >>> print(type(dataStr))
            <class 'str'>

        """
        return str(self.data)

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


# ------------------------------ Doubly Linked List ----------------------------


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
            >>> from DSA import DoublyLinkedListNode
            >>> Node = DoublyLinkedListNode(10)
            >>> dataStr = Node.__str__()
            >>> print(dataStr)
            10
            >>> print(type(dataStr))
            <class 'str'>

        """
        return str(self.data) 

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


# -------------------------- Binary Search Tree ------------------------------


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


# --------------------------------- Suffix Trie --------------------------------

class Trie:
    """
    | *The Trie Data Structure*
    | A Trie is used for *text processing*. It is an efficient information
      retrieval data structure which can store strings and search them optimally
    | Available functions on a Trie object are -
        
    - ``insert``  - Insert a new string into Trie
    - ``find`` - Find a particular string in Trie
    - ``checkPrefix`` - Check if a given prefix is present in the Trie
    - ``countPrefix`` -  Count number of Prefix of a string in the Trie
    
    """
    def __init__(self):
        """
        Constructor to construct a new empty Trie object

        :Example:
            >>> trie = Trie()
            >>> print(trie.T)
            {}
        """
        self.T = {}
    
    def find(self, root, c):
        """
        Find a particular string in Trie

        :param root: Trie Node starting from which it will find
        :param c: Text which is to be found
        :type root: dict
        :type c: str

        :return: True - If the character is found
        :return: False - If the character is not found
        :rtype: bool

        :Example:
            >>> trie = Trie()
            >>> trie.insert("I")
            >>> trie.insert("am")
            >>> trie.insert("Atishay")
            >>> trie.find(trie.T,"Atishay")
            True
            >>> trie.find(trie.T,"ABCD")
            False
        """
        currNode = root
        for i in c:
            if not i in currNode:
                return False
            else:
                currNode = currNode[i]
        return True
    
    def insert(self, s):
        """
        Insert a new word into Trie

        :param s: The string of word that is to be inserted
        :type s: str

        :Example:
            >>> trie = Trie()
            >>> trie.insert("I")
            >>> trie.insert("am")
            >>> trie.insert("Atishay")
            >>> print(trie.T["a"])
            {'#': 1, 'm': {'#': 1}}
        """
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s):
        """
        Function to check if a given prefix is present in the Trie

        :param s: The prefix which is to be searched in the Trie
        :type s: str
        :return: True - If the prefix is found
        :return: False - If the prefix is not found
        :rtype: bool

        :Example:
            >>> trie = Trie()
            >>> trie.insert("I")
            >>> trie.insert("am")
            >>> trie.insert("Atishay")
            >>> trie.checkPrefix("Ati")
            True
            >>> trie.checkPrefix("IIT")
            False
        """
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s):
        """
        Count number of Prefix of a string in the Trie

        :param s: String whose counts of prefix is to be counted
        :type s: str
        :return: Number of counts of Prefix
        :rtype: int

        :Example:
            >>> trie = Trie()
            >>> trie.insert("English")
            >>> trie.insert("England")
            >>> trie.insert("Engineer")
            >>> trie.countPrefix("Eng")
            3
            >>> trie.countPrefix("Engla")
            1
            >>> trie.countPrefix("Engo")
            0
        """
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0


# -------------------------------------- Heap --------------------------------------

class Heap:
    """
    This class implements the *Heap Data Structure*.
    A Heap is a special *Tree-based* data structure in which the tree is a Binary Tree that
    stores priorities (or priority-element) pairs at nodes. It has following properties :

    1. **Structural Property** : All levels except last are full. Last level is left-filled.
    2. **Heap Property** : Priority of node is at least as large as that of its parent.

    Operations/Member Functions of Heap Data Structure include:

    - **Heapify** : A process of creating a heap from an array.
    - **Insertion** : Process to insert an element in existing heap time complexity *O(log N)*.
    - **Deletion** : Deleting the top element of the heap or the highest priority element, and then organizing the heap and returning the element with time complexity *O(log N)*.
    - **Peek** : To check or find the most prior element in the heap, (max or min element for max and min heap).

    :param cap: Maximum Capacity of the Heap created
    :type cap: int
    :param H: Array being used for storing Heap
    :type H: list
    :param n: Number of elements in current Heap
    :param M: Maximum Capacity of Heap
    :type M: int
    :type n: int

    """
    def __init__(self, cap):
        """
        Contructor to initialize a new Heap object

        :param cap: Maximum Capacity of the Heap to be constructed
        :type cap: int
        
        :Example:
            >>> heap = Heap(10)
            >>> print(heap.M)
            10
            >>> print(heap.H)
            []
            >>> print(heap.n)
            0
        """
        self.n = 0
        self.M = cap
        self.H = []
    
    def parent(self, i):
        """
        Function to get the Parent Node's Index of an element in Heap

        :param i: Index of element whose Parent Node is to be found
        :type i: int
        :return: Index of the Parent Node
        :rtype: int
        
        :Example:
            >>> heap = Heap(10)
            >>> heap.insert(23)
            >>> heap.insert(45)
            >>> heap.insert(11)
            >>> heap.insert(56)
            >>> heap.insert(5)
            >>> print(heap.parent(3))
            1
        """
        return (i - 1) // 2
    
    def left(self, i):
        """
        Function to get the Left child's Index of a Node in Heap

        :param i: Index of element whose Left child is to be found
        :type i: int
        :return: Index of the Left child
        :rtype: int

        :Example:
            >>> heap = Heap(10)
            >>> heap.insert(23)
            >>> heap.insert(45)
            >>> heap.insert(11)
            >>> heap.insert(56)
            >>> heap.insert(5)
            >>> print(heap.left(1))
            3
        """
        return (2 * i) + 1
    
    def right(self, i):
        """
        Function to get the Right child's Index of a Node in Heap

        :param i: Index of element whose Right child is to be found
        :type i: int
        :return: Index of the Right child
        :rtype: int

        :Example:
            >>> heap = Heap(10)
            >>> heap.insert(23)
            >>> heap.insert(45)
            >>> heap.insert(11)
            >>> heap.insert(56)
            >>> heap.insert(5)
            >>> print(heap.right(1))
            4

        """
        return 2 * (i + 1)
    
    def insert(self, val):
        """
        Inserts a new Node into the Heap with a given value

        :param val: The value to be stored in the New Node
        :type val: auto
        
        :Example:
            >>> heap = Heap(10)
            >>> heap.insert(23)
            >>> heap.insert(45)
            >>> heap.insert(11)
            >>> heap.insert(56)
            >>> heap.insert(5)
            >>> print(heap.H)
            [5, 11, 23, 56, 45]
            >>> print(heap.n)
            5

        """
        if self.n != self.M:
            self.H.append(val)
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self):
        """
        | Function to get the Minimum value stored in the Heap.
        | Since Heap is implemented in such a way that the starting Node 
          has the minimum value according to the definition of Heap, 
          the minimum value to be returned is simply the value at 
          **first index** of the Heap.
        | `If Heap has zero elements, then -1 is returned`

        :return: Minimum value stored in Heap
        :rtype: auto
        
        :Example:
            >>> heap = Heap(10)
            >>> heap.insert(23)
            >>> heap.insert(45)
            >>> heap.insert(11)
            >>> heap.insert(56)
            >>> heap.insert(9)
            >>> print(heap.H)
            [9, 11, 23, 56, 45]
            >>> print(heap.min())
            9

        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """
        `Heapify` is a process of creating a Heap from a list of elements or Restoring 
        the Heap property if it is violated at any Node. Heapify at index `i` traces a path down the tree.
        All elements on path have lower priority than their siblings. All elements on this path are 
        moved up and element at index `i` is rearranged with them. This establishes Heap Property correctly.

        :param root: Index of Root Node, starting from which Heap will be made
        :type root: int
        
        :Example:
            >>> heap = Heap(10)
            >>> heap.H = [23,15,11,20,27]
            >>> print(heap.H)
            [23, 15, 11, 20, 27]
            >>> heap.n = 5
            >>> print(heap.n)
            5
            >>> heap.Heapify(0)
            >>> print(heap.H)
            [11, 15, 23, 20, 27]

        """
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self):
        """
        Deletes the Minimum Element. Notice that after deleting the 
        minimum element (`which was at the top`), there might bacome violation
        of heap property in some Nodes. Therefore, this function also rearranges
        the Heap accordingly using ``Heapify``
        
        :Example:
            >>> heap = Heap(10)
            >>> heap.insert(23)
            >>> heap.insert(45)
            >>> heap.insert(11)
            >>> heap.insert(56)
            >>> heap.insert(9)
            >>> print(heap.H)
            [9, 11, 23, 56, 45]
            >>> print(heap.n)
            5
            >>> heap.deleteMin()
            >>> print(heap.H)
            [11, 45, 23, 56]
            >>> print(heap.n)
            4
        """
        if self.n > 0:
            if self.n == 1:
                self.H = []
                self.n = 0
                self.H.pop()
            else:
                self.n -= 1
                self.H[0] = self.H[self.n]
                self.H.pop()
                self.Heapify(0)

