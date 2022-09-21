class Heap:
    """
    This class implements the Heap Data Structure.
    A Heap is a special Tree-based data structure in which the tree is a Binary Tree that
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
    """
    def __init__(self, cap):
        """
        Contructor
        """
        self.n = 0
        self.M = cap
        self.H = []
    
    def parent(self, i):
        """Function to get the Parent Node of an element in Heap

        :param i: Index of element whose Parent Node is to be found
        :type i: integer

        :return: Index of the Parent Node
        :rtype: integer

        """
        return (i - 1) // 2
    
    def left(self, i):
        """Function to get the Left child of a Node in Heap

        :param i: Index of element whose Left child is to be found
        :type i: integer
        
        :return: Index of the Left child
        :rtype: integer

        """
        return (2 * i) + 1
    
    def right(self, i):
        """Function to get the Right child of a Node in Heap

        :param i: Index of element whose Right child is to be found
        :type i: integer
        
        :return: Index of the Right child
        :rtype: integer

        """
        return 2 * (i + 1)
    
    def insert(self, val):
        """Inserts a new Node into the Heap with a given value

        :param val: The value to be stored in the New Node
        :type val: auto
        
        """
        if self.n != self.M:
            self.H.append(val)
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self):
        """Function to get the Minimum value stored in the Heap
        Since Heap is implemented in such a way that the root Node 
        has the minimum value according to the definition of Heap, 
        the minimum value to be returned is simply the value at 
        starting index of the Heap. `If Heap has zero elements, then
        -1 is returned`

        :return: Minimum value stored in Heap
        :rtype: auto
        
        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """Heapify is a process of creating a Heap from a list of elements or Restoring 
        the Heap property if it is violated at any Node. Heapify at index *i* traces a path down the tree.
        All elements on path have lower priority than their siblings. All elements on this path are 
        moved up and element at index *i* is rearranged with them. This establishes Heap Property correctly.

        :param root: Index of Root Node, starting from which Heap will be made
        :type root: integer
        
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
        """Deletes the Minimum Element. Notice that after deleting the 
        minimum element(`which was at the top`), there might bacome violation
        of heap property in some Nodes. Therefore, this function also rearranges
        the Heap accordingly using Heapify.
        
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