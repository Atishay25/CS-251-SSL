/**
 * @file DSA.h
 * @author Atishay Jain (atishay@cse.iitb.ac.in)
 * @brief Header file for Several Data Structures
 * @version 0.1
 * @date 2022-09-25
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <bits/stdc++.h>
#define ll long long int    /// Defined as a long long integer Data Type
#define vi vector<int>      /// A Vector of integer variables
#define vll vector<ll>      /// A Vector of long long integer variables  
using namespace std;

/** @brief Node of a Singly Linked List. Stores Data stored in 
    a Node and a pointer to its next Node*/
class SinglyLinkedListNode {

    public:

        /// Data stored in a Node
        ll data;
        /// Pointer to next Node
        SinglyLinkedListNode* next;
        
        /// Default Constructor
        SinglyLinkedListNode();
        
        /// @brief Constructor with a parameter
        /// @param val value of data to be stored in the Node
        SinglyLinkedListNode(ll val);

};

/// @brief Overloaded << operator to print the data of the Singly Linked List Node provided as arguement into a file
/// @param out File in which the Node data is printed
/// @param node The Singly Linked List Node whose data is to be printed
/// @return ostream& The File with the Node's data printed in it
ostream& operator<<(ostream &out, const SinglyLinkedListNode &node);

/**
 * @brief Singly Linked List Data Structure.
 */ 
/**
 * It is the simplest type of linked list in which every node contains 
 * some data and a pointer to the next node of the same data type. 
 * 
 */
class SinglyLinkedList {

    public:
    
        /// Head Node of the Linked List
        SinglyLinkedListNode *head, *tail;
        ///< Tail Node of the Linked List
        
        /// Construtor of a Singly Linked List
        SinglyLinkedList();
        
        /**
         * @brief Function to insert a New Node into the Linked List
         * 
         * @param[in] data value of Data to be stored in the new Node Inserted
         */
        void insert (ll data);
        
        /**
         * @brief Find Previous Node of a Node with a given data 
         * 
         * @param[in] data value of data to be found
         * @return Previous Node of the Node with given data (if found), else returns NULL
         */
        SinglyLinkedListNode* find (ll data);
        
        /**
         * @brief Delete the Node with given data
         * 
         * @param[in] data data stored in the Node which is to be deleted 
         * @return True - If data found in the Linked List and deleted
         * @return False - If data given is not found in the Linked List
         */
        bool deleteVal (ll data);
        
        /**
         * @brief Function to print the Linked List with a given separation
         * between the Data stored in each Node
         * 
         * @param[in] sep Separation to be used between Datam of each node
         *  while printing the linked list
         */
        void printer (string sep);

        /**
         * @brief Reverse the Order of Elements in the Linked List
         * 
         */
        void reverse ();

};

/**
 * @brief Function to Merge two Singly Linked Lists into one Singly Linked List
 * 
 * @param list1 First Linked List to be merged
 * @param list2 Second Linked List to be merged
 * @return SinglyLinkedList - Merged Singly Linked List
 */
SinglyLinkedList merge (SinglyLinkedList list1, SinglyLinkedList list2);


/* ------------------------------- Doubly Linked List ----------------------------- */

/**
 * @brief Node of a Doubly Linked List.
 * 
 */
/// @brief It Stores an additional pointer as compared to a 
///Singly Linked List Node, mainly to point to Previous Node as well
class DoublyLinkedListNode {

    public:
        
        /// @brief Data stored in the Node
        ll data;
        /// @brief Pointer to Next Node
        DoublyLinkedListNode *next, *prev;
        ///< Pointer to Previous Node
        
        /** @brief Default Contructor */
        /// It initializes :
        /// - data to -1
        /// - next to NULL
        /// - prev to NULL
        DoublyLinkedListNode();
        
        /**
         * @brief Construct a new Doubly Linked List Node object with a given value to be stored
         * 
         * @param val The value to be stored in the Node
         */
        /// It initializes : 
        /// - data to val
        /// - next to NULL
        /// - prev to NULL
        DoublyLinkedListNode(ll val);

};

/**
 * @brief  Overloaded << operator to print the data of the 
 * Doubly Linked List Node provided as arguement into a file
 * @param out File in which the Node data is printed
 * @param node The Doubly Linked List Node whose data is to be printed
 * @return ostream& The File with the Node's data printed in it
 */
ostream& operator<<(ostream &out, const DoublyLinkedListNode &node);

/**
 * @brief Doubly Linked List Data Structure.
 * 
 */
/**
 * A Doubly Linked List (DLL) contains an extra pointer, typically 
 * called the previous pointer, together with the next pointer and 
 * data which are there in the singly linked list.
 */
class DoublyLinkedList {

    public:
        
        /// @brief Head Node i.e. The Node at starting Index
        DoublyLinkedListNode *head, *tail;
        ///< Tail Node i.e. The Node at last Index
        
        /**
         * @brief Construct a new Doubly Linked List object
         * 
         */
        /** Sets head and tail to NULL*/
        DoublyLinkedList ();
        
        /**
         * @brief Insert new Node with a given data into the Linked List
         * 
         * @param data Data to be stored into the New Node 
         */
        void insert (ll data);
        
        /**
         * @brief Function to print the Linked List with a given separation
         * between the Data stored in each Node
         * 
         * @param[in] sep Separation to be used between Datam of each node
         *  while printing the linked list
         */
        void printer (string sep);
        
        /**
         * @brief Reverse the Order of Elements in the Linked List
         * 
         */
        void reverse ();

};

/* ------------------------------- Binary Search Tree ----------------------------- */

/**
 * @brief Node of a Binary Search Tree
 * 
 */
class BSTNode {

    public:

        /// @brief Data stored in the Node
        ll info, level; ///< @brief Height of the Node

        /// Pointer to the Left Child of the Node
        BSTNode *left, *right; ///< Pointer to the Right Child of the Node
        
        /**
         * @brief Construct a new BSTNode object with a given value stored in it
         * 
         * @param val Data to be stored in the BSTNode
         */
        BSTNode (ll val);

};

/**
 * @brief  Overloaded << operator to print the data of the 
 * Binary Search Tree Node provided as arguement into a file
 * @param out File in which the Node data is printed
 * @param node The BSTNode whose data is to be printed
 * @return ostream& The File with the Node's data printed in it
 */
ostream& operator<<(ostream &out, const BSTNode &node);

/**
 * @brief Binary Search Tree Data Structure
 * 
 */
/**
 * BST is a Binary Tree Data Structure in which -
 * 1. Left Subtree of each Node stores Nodes with values lesser than the Node
 * 2. Right Subtree of each Node stores Nodes with values greater than the Node
 * 3. Left and Right Subtree each must also be a Binary Search Tree
 */
class BinarySearchTree {

    public:
        
        /// @brief Root Node of BST
        BSTNode *root;
        
        /// @brief Order of Traversal in BST
        enum order {
            PRE /// Current Node, left, right
            , IN /// left, Current Node, right
            , POST /// left, right, Current Node
        };
        
        /** @brief Default Constructor */
        /// Initializes root to NULL
        BinarySearchTree ();
        
        /**
         * @brief Insert a New Node in BST with a given Value
         * 
         * @param val Value to be stored in New Node
         */
        void insert(ll val);
        
        /**
         * @brief Print the Values stored in BST in a given Traversal Order
         * 
         * @param T Node starting from which the Tree is to be printed 
         * @param tt Order of Traversal of Tree. It can be -
         * 1. Pre Order
         * 2. In Order
         * 3. Post Order
         */
        void traverse (BSTNode* T, order tt);
        
        /**
         * @brief Function to get the Height of a given Node.
         * Height here is defined as the longest distance of a 
         * Node to a leaf.
         * 
         * @param T Node whose height is to be found
         * @return Height of the given Node
         */
        ll height(BSTNode *T);

};

/* ----------------------------------- Suffix Trie --------------------------------- */

/**
 * @brief The Trie Data Structure
 * 
 */
/**
 * A Trie is used for text processing. It is an efficient information
 * retrieval data structure which can store strings and search them optimally
 */
class Trie {

    public:
        
        /**
         * @brief Number of total Nodes in Trie
         * 
         */
        ll count;

        /// @brief Map of Trie Nodes and characters, in which
        /// a character is mapped to a Trie Pointer
        map<char,Trie*> nodes;
        
        /**
         * @brief Default Constructor to construct a new Trie object
         */
        Trie ();
        
        /**
         * @brief Find a particular character in Trie
         * 
         * @param[in] T Trie Node starting from which it will start finding
         * @param[in] c character which is to be found
         * @return True - If the character is found
         * @return False - If the character is not found
         */
        bool find(Trie* T, char c);
        
        /**
         * @brief Insert a new word into Trie
         * 
         * @param s The string of word that is to be inserted
         */
        void insert(string s);
        
        /**
         * @brief Function to check if a given prefix is present in the Trie
         * 
         * @param s The prefix which is to be searched in the Trie
         * @return True - If the prefix is found
         * @return False - If the prefix is not found
         */
        bool checkPrefix(string s);
        
        /**
         * @brief Function to count number of Prefix in Trie of a string
         * 
         * @param s The string whose counts of prefix is to be counted
         * @return The number of counts of Prefix 
         */
        ll countPrefix(string s);

};

/*------------------------------------ Heap ---------------------------------------- */

/**
 * @brief This class implements the Heap Data Structure.
 * 
 */
/**
 * A Heap is a special Tree-based data structure in which the tree is a Binary Tree that
    stores priorities (or priority-element) pairs at nodes.
 */

class Heap {

    public:

        /// @brief Number of elements in current Heap
        int n;
        /// @brief Maximum Capacity of Heap
        int Cap;
        /// @brief  Array in which Heap elements are stored
        int *arr;

        /**
         * @brief Construct a new Heap object
         * 
         * @param cap The Maximum Capacity of Heap
         */
        Heap(int cap);

        /// @brief Function to get the Parent Node of an element in Heap
        /// @param i Index of element whose Parent Node is to be found
        /// @return Index of the Parent Node
        int parent(int i);

        /// @brief Function to get the Left child of a Node in Heap
        /// @param i Index of element whose Left child is to be found
        /// @return Index of the Left child
        int left(int i);

        /// @brief Function to get the Right child of a Node in Heap
        /// @param i Index of element whose Right child is to be found
        /// @return Index of the Right child
        int right(int i);

        /**
         * @brief Inserts a new Node into the Heap with a given value
         * 
         * @param val The value to be stored in the New Node
         */
        void insert(int val);

        /**
         * @brief Function to get the Minimum value stored in the Heap
         * 
         * @return Minimum value stored in Heap
         */
        int min();

        /**
         * @brief Heapify is a process of creating a Heap from a list of elements or Restoring 
         * the Heap property if it is violated at any Node. This function implements
         * Heapify on the present Heap from a given node.
         * 
         * @param root Index of Node, starting from which Heap will be made
         */
        void Heapify(int root);

        /**
         * @brief Deletes the Minimum Element and Heapifies the heap 
         * after deleting the minimum element.
         * 
         */
        void deleteMin();

};


