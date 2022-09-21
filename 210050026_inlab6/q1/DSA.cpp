/**
 * @file DSA.cpp
 * @author Atishay Jain (atishay@cse.iitb.ac.in)
 * @brief DSA Library consisting of implementation of several Data Structures including
 * Binary Search Tree, Linked Lists (Single and Double) and Trie
 * @version 0.1
 * @date 2022-09-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <bits/stdc++.h> 

/// Defined as a long long integer Data Type
#define ll long long int

/// A Vector of integer variables
#define vi vector<int>

/// A Vector of long long integer variables  
#define vll vector<ll>

using namespace std;

/* ------------------------------- Data Structures ---------------------------------- */

// ------------------------------- Singly Linked List -----------------------------

/** @brief Node of a Singly Linked List. Stores Data stored in 
    a Node and a pointer to its next Node*/
class SinglyLinkedListNode {

    public:
        /// Data stored in a Node
        ll data; 
        /// Pointer to next Node
        SinglyLinkedListNode* next;
        
        /// @brief Default Constructor
        SinglyLinkedListNode () {
            /// Initializes "data" stored to -1 and "next" pointer to NULL 
            data = -1;
            next = NULL;
        }
        
        /// @brief Constructor with a parameter
        /// @param val - value of data to be stored in the Node
        SinglyLinkedListNode (ll val) {
            /// @brief Initializes "data" stored to "val" and "next" pointer to NULL 
            data = val;
            next = NULL;
        }

};

/// @brief Overloaded << operator to print the data of the Singly Linked List Node provided as arguement into a file
/// @param[in] out - File in which the Node data is printed
/// @param[in] node - The Singly Linked List Node whose data is to be printed
/// @return ostream& The File with the Node's data printed in it
ostream& operator<<(ostream &out, const SinglyLinkedListNode &node) {
    return out << node.data;
}

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
        SinglyLinkedList () {
            /// @brief Sets head and tail to NULL
            head = NULL;
            tail = NULL;
        }
        
        /**
         * @brief Function to insert a New Node into the Linked List
         * 
         * @param[in] data - value of Data to be stored in the new Node Inserted
         */
        void insert (ll data) {
            SinglyLinkedListNode *node = new SinglyLinkedListNode(data);
            if (head == NULL) {
                head = node;
            }
            else {
                tail -> next = node;
            }
            tail = node;
        }
        
        /**
         * @brief Find Previous Node of a Node with a given data 
         * 
         * @param[in] data - value of data to be found
         * @return Previous Node of the Node with given data (if found), else returns NULL
         */
        SinglyLinkedListNode* find (ll data) {
            SinglyLinkedListNode *ptr = head, *prev = NULL;
            while (ptr != NULL && ptr -> data != data) {
                prev = ptr;
                ptr = ptr -> next;
            }
            return prev;
        }
        
        /**
         * @brief Delete the Node with given data
         * 
         * @param[in] data - data stored in the Node which is to be deleted 
         * @return true - If data found in the Linked List and deleted
         * @return false - If data given is not found in the Linked List
         */
        bool deleteVal (ll data) {
            SinglyLinkedListNode *prev = find(data);
            if (prev -> next == NULL) {
                return false;
            }
            prev -> next -> next = prev -> next;
            return true;
        }
        
        /**
         * @brief Function to print the Linked List with a given separation
         * between the Data stored in each Node
         * 
         * @param[in] sep - Separation to be used between Datam of each node
         *  while printing the linked list
         */
        void printer (string sep = ", ") {
            SinglyLinkedListNode *ptr = head;
            cout << "[";
            while (ptr != NULL) {
                cout << *ptr;
                ptr = ptr -> next;
                if (ptr != NULL) {
                    cout << sep;
                }
            }
            cout << "]\n";
        }
        
        /**
         * @brief Reverse the Order of Elements in the Linked List
         * 
         */
        void reverse () {
            SinglyLinkedListNode *ptr = head, *prev = NULL;
            while (ptr != NULL) {
                SinglyLinkedListNode *ptr2 = ptr -> next;
                ptr -> next = prev;
                prev = ptr;
                ptr = ptr2;
            }
            tail = ptr;
            head = prev;
        }

};

/**
 * @brief Function to Merge two Singly Linked Lists into one Singly Linked List
 * 
 * @param list1 - First Linked List to be merged
 * @param list2 - Second Linked List to be merged
 * @return SinglyLinkedList - Merged Singly Linked List
 */
SinglyLinkedList merge (SinglyLinkedList list1, SinglyLinkedList list2) {
    SinglyLinkedList merged;
    SinglyLinkedListNode *head1 = list1.head, *head2 = list2.head;
    while (head1 != NULL && head2 != NULL) {
        if (head1 -> data < head2 -> data) {
            merged.insert(head1 -> data);
            head1 = head1 -> next;
        }
        else {
            merged.insert(head2 -> data);
            head2 = head2 -> next;
        }
    }
    if (head1 == NULL && head2 != NULL) {
        merged.tail -> next = head2;
    }
    if (head2 == NULL && head1 != NULL) {
        merged.tail -> next = head1;
    }
    return merged;
}

// ------------------------------- Doubly Linked List -----------------------------

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
        DoublyLinkedListNode () {
            data = -1;
            next = NULL;
            prev = NULL;
        }
        
        /**
         * @brief Construct a new Doubly Linked List Node object with a given value to be stored
         * 
         * @param val - The value to be stored in the Node
         */
        DoublyLinkedListNode (ll val) {
            /// It initializes : 
            /// - data to val
            /// - next to NULL
            /// - prev to NULL
            data = val;
            next = NULL;
            prev = NULL;
        }

};

/**
 * @brief  Overloaded << operator to print the data of the 
 * Doubly Linked List Node provided as arguement into a file
 * @param out - File in which the Node data is printed
 * @param node - The Doubly Linked List Node whose data is to be printed
 * @return ostream& The File with the Node's data printed in it
 */
ostream& operator<<(ostream &out, const DoublyLinkedListNode &node) {
    return out << node.data;
}

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
        DoublyLinkedList () {
            /// @brief Sets head and tail to NULL
            head = NULL;
            tail = NULL;
        }
        
        /**
         * @brief Insert new Node with a given data into the Linked List
         * 
         * @param data - Data to be stored into the New Node 
         */
        void insert (ll data) {
            DoublyLinkedListNode *node = new DoublyLinkedListNode(data);
            if (head == NULL) {
                head = node;
            }
            else {
                tail -> next = node;
                node -> prev = tail;
            }
            tail = node;
        }
        
        /**
         * @brief Function to print the Linked List with a given separation
         * between the Data stored in each Node
         * 
         * @param[in] sep - Separation to be used between Datam of each node
         *  while printing the linked list
         */
        void printer (string sep = ", ") {
            DoublyLinkedListNode *ptr = head;
            cout << "[";
            while (ptr != NULL) {
                cout << *ptr;
                ptr = ptr -> next;
                if (ptr != NULL) {
                    cout << sep;
                }
            }
            cout << "]\n";
        }
        
        /**
         * @brief Reverse the Order of Elements in the Linked List
         * 
         */
        void reverse () {
            DoublyLinkedListNode *ptr = head, *pr = NULL;
            while (ptr != NULL) {
                DoublyLinkedListNode *ptr2 = ptr -> next;
                if (ptr2 != NULL) {
                    ptr2 -> prev = ptr;
                }
                ptr -> next = pr;
                ptr -> prev - ptr2;
                pr = ptr;
                ptr = ptr2;
            }
            tail = ptr;
            head = pr;
        }

};

// ------------------------------- Binary Search Tree -----------------------------

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
         * @param val - Data to be stored in the BSTNode
         */
        BSTNode (ll val) {
            info = val;
            level = 0;
            left = NULL;
            right = NULL;
        }

};

/**
 * @brief  Overloaded << operator to print the data of the 
 * Binary Search Tree Node provided as arguement into a file
 * @param out - File in which the Node data is printed
 * @param node - The  BSTNode whose data is to be printed
 * @return ostream& The File with the Node's data printed in it
 */
ostream& operator<<(ostream &out, const BSTNode &node) {
    return out << node.info;
}

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
        
        /// @brief Default Constructor
        BinarySearchTree () {
            /// Initializes root to NULL
            root = NULL;
        }
        
        /**
         * @brief Insert a New Node in BST with a given Value
         * 
         * @param val - Value to be stored in New Node
         */
        void insert(ll val) {
            if (root == NULL) {
                root = new BSTNode(val);
            }
            else {
                BSTNode *ptr = root;
                while (true) {
                    if (val < ptr -> info) {
                        if (ptr -> left != NULL) {
                            ptr = ptr -> left;
                        }
                        else {
                            ptr -> left = new BSTNode(val);
                            break;
                        }
                    }
                    else if (val > ptr -> info) {
                        if (ptr -> right != NULL) {
                            ptr = ptr -> right;
                        }
                        else {
                            ptr -> right = new BSTNode(val);
                            break;
                        }
                    }
                    break;
                }
            }
        }
        
        /**
         * @brief Print the Values stored in BST in a given Traversal Order
         * 
         * @param T - Node starting from which the Tree is to be printed 
         * @param tt - Order of Traveral of Tree. It can be -
         * 1. Pre Order
         * 2. In Order
         * 3. Post Order
         */
        void traverse (BSTNode* T, order tt) {
            if (tt == PRE) {
                cout << T << endl;
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
            }
            else if (tt == IN) {
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                cout << T << endl;
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
            }
            else if (tt == POST) {
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
                cout << T << endl;
            }
        }
        
        /**
         * @brief Function to get the Height of a given Node.
         * Height here is defined as the longest distance of a 
         * Node to a leaf.
         * 
         * @param T - Node whose height is to be found
         * @return Height of the given Node
         */
        ll height(BSTNode *T) {
            if (T -> left == NULL && T -> right == NULL) {
                return 0;
            }
            else if (T -> right == NULL) {
                return 1 + height(T -> left);
            }
            else if (T -> left == NULL) {
                return 1 + height(T -> right);
            }
            return max(1 + height(T -> left),1 + height(T -> right));
        }

};

// ------------------------------- Suffix Trie -----------------------------

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
        Trie () {
            count = 0;
            nodes = map<char,Trie*>();
        }
        
        /**
         * @brief Find a particular character in Trie
         * 
         * @param[in] T - the Trie Node starting from which it will start finding
         * @param[in] c - character which is to be found
         * @return true - If the character is found
         * @return false - If the character is not found
         */
        bool find(Trie* T, char c) {
            return ((T -> nodes).find(c) != (T -> nodes).end());
        }
        
        /**
         * @brief Insert a new word into Trie
         * 
         * @param s - The string of word that is to be inserted
         */
        void insert(string s) {
            Trie* ptr = this;
            for (auto c: s) {
                if (!find(ptr,c)) {
                    (ptr -> nodes)[c] = new Trie();
                }
                ptr = (ptr -> nodes)[c];
                (ptr -> count)++;
            }
        }
        
        /**
         * @brief Function to check if a given prefix is present in the Trie
         * 
         * @param s - The prefix which is to be searched in the Trie
         * @return true - If the prefix is found
         * @return false - If the prefix is not found
         */
        bool checkPrefix(string s) {
            Trie* ptr = this;
            for (ll i = 0; i < s.length(); i++) {
                if (!find(ptr,s[i])) {
                    if (i == s.length() - 1) {
                        (ptr -> nodes)[s[i]] = NULL;
                    }
                    else {
                        (ptr -> nodes)[s[i]] = new Trie();
                    }
                }
                else if ((ptr -> nodes)[s[i]] == NULL or i == s.length() - 1) {
                    return true;
                }
                ptr = (ptr -> nodes)[s[i]];
            }
            return false;
        }
        
        /**
         * @brief Function to count number of Prefix in Trie of a string
         * 
         * @param s - The string whose counts of prefix is to be counted
         * @return The number of counts of Prefix 
         */
        ll countPrefix(string s) {
            bool found = true;
            Trie* ptr = this;
            for (auto c: s) {
                if (find(ptr,c)) {
                    ptr = (ptr -> nodes)[c];
                }
                else {
                    found = false;
                    break;
                }
            }
            if (found) {
                return ptr -> count;
            }
            return 0;
        }

};

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
         * @param cap - The Maximum Capacity of Heap
         */
        Heap(int cap){
            n = 0;
            Cap = cap;
            arr = new int[Cap];
        }

        /// @brief Function to get the Parent Node of an element in Heap
        /// @param i - Index of element whose Parent Node is to be found
        /// @return Index of the Parent Node
        int parent(int i){
            return (i-1)/2;
        }

        /// @brief Function to get the Left child of a Node in Heap
        /// @param i - Index of element whose Left child is to be found
        /// @return Index of the Left child
        int left(int i){
            return (2*i) + 1;
        }

        /// @brief Function to get the Right child of a Node in Heap
        /// @param i - Index of element whose Right child is to be found
        /// @return Index of the Right child
        int right(int i){
            return 2*(i+1);
        }

        /**
         * @brief Inserts a new Node into the Heap with a given value
         * 
         * @param val  The value to be stored in the New Node
         */
        void insert(int val){
            if(n != Cap){
                arr[n] = val;
                int i = n;
                n++;
                int temp;
                while(i != 0 && arr[parent(i)] > arr[i]){
                    temp = arr[i];
                    arr[i] = arr[parent(i)];
                    arr[parent(i)] = temp;
                    i = parent(i);
                }
            }
        }

        /**
         * @brief Function to get the Minimum value stored in the Heap
         * 
         * @return Minimum value stored in Heap
         */
        int min(){
            if(n != 0) return arr[0];
            else return -1;
        }

        /**
         * @brief Heapify is a process of creating a Heap from a list of elements or Restoring 
         * the Heap property if it is violated at any Node. This function implements
         * Heapify on the present Heap from a given node.
         * 
         * @param root Index of Node, starting from which Heap will be made
         */
        void Heapify(int root){
            int l = left(root);
            int r = right(root);
            int s = root;
            if(l < n && arr[l] < arr[root]) s = l;
            if(r < n && arr[r] < arr[s]) s = r;
            if(s != root){
                int temp = arr[root];
                arr[root] = arr[s];
                arr[s] = temp;
                Heapify(s);
            }
        }

        /**
         * @brief Deletes the Minimum Element and Heapifies the heap 
         * after deleting the minimum element.
         * 
         */
        void deleteMin(){
            if(n > 0){
                if(n == 1){
                    n = 0;
                    arr[0] = 0;
                }
                else{
                    arr[n] = 0;
                    n--;
                    arr[0] = arr[n];
                    Heapify(0);
                }
            }
        }

};
