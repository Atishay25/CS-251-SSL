##############################################
"""
Extra functions or variables if required

"""
##############################################

from signal import raise_signal
from exception import Lab5Exception


def rotate(arr):

    rotated_array = []
    n = len(arr)
    m = len(arr[0])
    if(n < 1):
        raise Lab5Exception("Order of matrix is less than 1")
    if(n != m):
        raise Lab5Exception("Matrix provided is not a Square Matrix")
    for i in arr:
        if(len(i) != m):
            raise Lab5Exception("Not a valid Matrix")
    for i in range(n-1,-1,-1):
        l = list()
        for j in arr:
            l.append(j[i])
        rotated_array.append(l)
    return rotated_array

    """
    This function takes a list of lists as input and returns the rotated verion 
    (rotated 90 degrees anti-clockwise)

    Input arguments:
    arr : List of lists

    Returns: rotated_array

    """

################################### Add your code here ###################################

##########################################################################################

    


# Use the main() function only for testing your code

if __name__ == "__main__":
    
    """
    Main function

    Example call:
    You can use the following matrix "test_arr" for testing your solution.
    For running the code, use the command "python q1.py" 
    """
    test_arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    #test_arr = [[3,2,7],[4,5,6],[5,6,7,8]]
    #test_arr = [[1, 2, 3, 4,12,90], [5, 6, 68,7, 8,97], [9, 10, 11, 68,12,54], [13, 14, 15, 67,16,22],[2,4,5,2,1,987],[6 ,7 ,5 ,1 ,9 ,8]]
    rotated_array = rotate(test_arr)
    print(rotated_array)
    """
    Console output should be: [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]

    """