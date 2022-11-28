import sys, os
sys.path.append(os.path.relpath('../'))
from exception import Lab5Exception

def add(arg1, arg2):
    r"""
        This function accepts two arguments - arg1 and arg2.
        It returns the result of the operation (arg1 + arg2).

        You are expected to think of corner cases,
        and appropriately raise Exception.
    """
    if not (type(arg1) == float or type(arg1) == int or type(arg1) == complex):
        raise Lab5Exception("Non-numeric arguements provided")
    if not (type(arg2) == float or type(arg2) == int or type(arg2) == complex):
        raise Lab5Exception("Non-numeric arguements provided")
    return arg1 + arg2

def subtract(arg1, arg2):
    r"""
        This function accepts two arguments - arg1 and arg2.
        It returns the result of the operation (arg1 - arg2).

        As the previous function, you are expected to think of corner cases,
        and appropriately raise Exception.
    """
    if not (type(arg1) == float or type(arg1) == int or type(arg1) == complex):
        raise Lab5Exception("Non-numeric arguements provided")
    if not (type(arg2) == float or type(arg2) == int or type(arg2) == complex):
        raise Lab5Exception("Non-numeric arguements provided")
    return arg1 - arg2

def divide(arg1, arg2):
    r"""
        This function accepts two arguments - arg1 and arg2.
        It returns the result of the operation (arg1 / arg2).

        You are expected to think of corner cases, and appropriately raise Exception.
    """
    if not (type(arg1) == float or type(arg1) == int or type(arg1) == complex):
        raise Lab5Exception("Non-numeric arguements provided")
    if not (type(arg2) == float or type(arg2) == int or type(arg2) == complex):
        raise Lab5Exception("Non-numeric arguements provided")
    if arg2 == 0:
        raise Lab5Exception("Division by zero is not possible")
    return arg1/arg2

def str_left_rotate(arg1, arg2):
    r"""
        This function should left rotate a string by the specified amount.
        arg1 signifies the input string and arg2 signifies the amount of rotation.

        Example - 
        1. str_left_rotate("hello", 2) should return "llohe"
        2. str_left_rotate("hello", 1) should return "elloh"
        3. str_left_rotate("hello", 4) should return "ohell" and so on

        You are not to use any inbuilt string method, the implementation has to be
        done by you!!

        Again, you are expected to think of corner cases, and appropriately raise Exception.
    """
    # raise exception for negative arg2!!
    # can check for type of args, like str_left_rotate("bencho",7.8)
    # check empty strings
    if type(arg1) != str:
        raise Lab5Exception("String to be rotated is not of str data type")
    if type(arg2) != int:
        raise Lab5Exception("Rotation amount given is not an integer")
    if arg2 < 0:
        raise Lab5Exception("Negative rotation amount provided") 
    rotated_str = ""
    for i in range(len(arg1)):
        rotated_str += arg1[(i+arg2)%len(arg1)]
    return rotated_str

def apply(fn, args):
    r"""
        This is the API end-point available to the grader.
        The grader will supply the function pointer to this function,
        along with the arguments and expect the return value.

        Example - 
        1. apply(add, (2, 3)) will expect 5 as the answer.
        2. apply(subtract, (2, 3)) will expect -1 as the answer.
    """
    if not (type(args) == tuple or type(args) == list):
        raise Lab5Exception("Arguements provided are not in a tuple/list") 
    if len(args) != 2:
        raise Lab5Exception("2 Arguements are not provided")
    return fn(args[0],args[1])

