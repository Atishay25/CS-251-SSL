from curses.ascii import isalpha
from unicodedata import numeric
from exception import Lab5Exception

def validSet(col1, col2):
    """
        This function checks validity of the collections as a set.
        If any collection has two or more same elements
        then exception is raised.
    """
    col2test = list()
    col1test = list()
    for i in col2:
        if not i in col2test:
            col2test.append(i)
    if len(col2test) != len(col2):
        raise Lab5Exception("List/Tuple does not satisfy fundamental property of Set")
    for i in col1:
        if not i in col1test:
            col1test.append(i)
    if len(col1test) != len(col1):
        raise Lab5Exception("List/Tuple does not satisfy fundamental property of Set")

def set_union(collection_one, collection_two):
    """
        This function, as the name implies, should output 
        the result of union of two sets. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    union = list()
    col2 = list(collection_two)
    col1 = list(collection_one)
    validSet(col1,col2)
    union = col1 + col2
    intersection = set_intersection(collection_one,collection_two)
    for j in intersection:
        if j in union:
            union.remove(j)
    return union

def set_intersection(collection_one, collection_two):
    """
        This function, as the name implies, should output 
        the result of intersection of two sets. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    intersection = list()
    col2 = list(collection_two)
    col1 = list(collection_one)
    validSet(col1,col2)
    for i in collection_one:
        for j in collection_two:
            if i == j:
                intersection.append(i)
    return intersection

def set_equality(collection_one, collection_two):
    """
        This function, as the name implies, should check whether
        or not two sets are equal. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    validSet(list(collection_one),list(collection_two))
    for i in collection_one:
        if not i in collection_two:
            return False
    for i in collection_two:
        if not i in collection_one:
            return False
    return True

def parse_file(file_name):
    """
        This function is expected to parse a text (.txt) file
        and extract pairs of collections from it.

        Note that the parsed collections might not be valid sets.
        Please check and accordingly raise Exception. You should also
        think about other corner cases of your code and raise the Exception
        accordingly.
    """
    final = list()
    with open(file_name,'r') as f:    
        for line in f:
            l1 = line.rstrip().split("    ")
            l = []
            for i in l1:
                l.append(eval(i))
            validSet(l[0],l[1])
            final.append(l)
    return final
