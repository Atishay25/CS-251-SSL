# Running your solution - You can run this script in console with the command given in the next line
# python q2.py 10
# Here 10 is the input provided by the user. Hence the output should be the list of prime numbers less than or equal to 10. Your console output shpuld be:
# List of primes = [2,3,5,7]

########################################## Script starts here ########################################
import argparse
from functools import reduce
import matplotlib.pyplot as plt
# This python module can be used for getting the input provided by user

parser = argparse.ArgumentParser()
parser.add_argument('number',type=int)
args = parser.parse_args()
num = args.number

numbers = list(range(2,num+1))
primeNumbers = list()
def checkprime(x,y):
   global numbers, primeNumbers
   if(len(numbers) == 0): 
      return
   if(len(numbers) > 0):
      primeNumbers.append(numbers[0])
   var = numbers[0]
   numbers = list(filter(lambda x: x % var, numbers))
   

def get_primes(num):
   # Should take an integer as input and reutrn a list of primes less than or equal to the given input

   # the variable num should be declared before the main() function as a global variable
   
   prime_number = 2
   is_prime = [prime_number]
   prime = list(filter(lambda x: x % prime_number, is_prime))
   return reduce(checkprime,numbers)



if __name__ == '__main__':
   # Edit this part of the code in order to pass the argument to get_primes() function
   # num is the argument you got from command line using argparse module
   get_primes(num)
   print("List of primes =",primeNumbers)
   plt.plot(primeNumbers,primeNumbers,"ob")
   plt.title("Prime Numbers till " + str(num))
   plt.show()
    
    
