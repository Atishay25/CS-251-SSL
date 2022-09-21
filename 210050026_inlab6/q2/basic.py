def binarySearch(arr, val):
    """Function to search for a given value in a list using **Binary Search**
    algorithm and return the index at which the value is found.
    If the value is not found, it returns *-1*. This algorithm is used
    if the list is sorted. It uses the fact that if the wanted element
    is lesser/greater than the middle element then it will be present
    to the left/right of middle element in a sorted List.

    :param arr: The Array in which a given Value is to be searched
    :type arr: int
    :param val: The integer value which is to be searched in the list
    :type val: int
    :return: The index of the value (if found), else *-1* (if not found)
    :rtype: int
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] > val:
            r = m-1
        elif arr[m] < val:
            l = m+1
        else:
            return m
    return -1

