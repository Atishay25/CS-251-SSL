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
