#python program ot find the power of a number using recursion.


#Given a number N and power P, the task is to find the power of a number ( i.e. NP ) using recursion.

#Examples: 

#Input: N = 2 , P = 3
#Output: 8

#Input: N = 5 , P = 2
#Output: 25



#Approach: Below is the idea to solve the above problem:

#The idea is to calculate power of a number ‘N’ is to multiply that number ‘P’ times.

#Follow the below steps to Implement the idea:



#reate a recursive function with parameters number N and power P.
#If P = 0 return 1.
#Else return N times result of the recursive call for N and P-1.
#Below is the implementation of the above approach.

# Python3 code to recursively find
# the power of a number

# Recursive function to find N^P.
def power(N, P):

    # If power is 0 then return 1
    # if condition is true
    # only then it will enter it,
    # otherwise not
    if P == 0:
        return 1

    # Recurrence relation
    return (N*power(N, P-1))


# Driver code
if __name__ == '__main__':
    N = 5
    P = 2

    print(power(N, P))
