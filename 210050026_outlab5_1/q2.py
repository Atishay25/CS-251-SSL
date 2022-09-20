#######################################

"""
Import any libraries if required
Extra functions or variables if required

"""
def maxLen(L):
    """
        Function to calculate length of maximum
        sub-list present in the given list.
    """
    max = 0
    for j in L:
        if(len(j) >= max):
            max = len(j)
    return max

#######################################

def weirdProblem(L):
    """
    This function takes a list of lists as input and returns a string which is a
    concatenation of elements 
    Input arguments:
    L : List of lists
    Returns: converted_string
	string
    """
    converted_string = ""
    n = maxLen(L)
    for j in range(0,n):
        for i in L:
            if(j < len(i)):
                converted_string = converted_string + i[j] + " "
    return converted_string

################################### Add your code here ###################################

##########################################################################################


if __name__ == "__main__":

    """
    Main function

    Example call:
    You can use the following list of lists "L" for testing your solution.
    For running the code, use the command "python q2.py" 
    """
    L = [ ["this", "programming", "is"], ["is", "assignment", "kinda"], ["a", "which", "weird"]  ]
    #L = [ ["this", "programming"],["is", "assignment", "is"], ["a", "which", "kinda" ,"weird"] ]
    #L = [ ["Hey!","Outlab5","1","of","Jain"], ["This","Python","submission","Atishay"], ["is","part"]]
    converted_string = weirdProblem(L)
    print(converted_string)
    
    """

    Console output should be: this is a programming assignment which is kinda weird

    """
