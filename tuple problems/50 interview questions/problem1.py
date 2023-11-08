#Python | Print unique rows in a given boolean matrix using Set with tuples

#Last Updated : 28 Jul, 2022
#Given a binary matrix, print all unique rows of the given matrix. Order of row printing doesn’t matter. 

#Examples:

#Input:
#    mat = [[0, 1, 0, 0, 1],
#             [1, 0, 1, 1, 0],
#             [0, 1, 0, 0, 1],
#             [1, 1, 1, 0, 0]]
#Output:
#          (1, 1, 1, 0, 0)
#          (0, 1, 0, 0, 1)
#          (1, 0, 1, 1, 0)



#We have existing solution for this problem please refer link. We can solve this problem in python quickly using Set data structure. Approach is very simple.

#We are given list of boolean values list, put all rows (list) in set because set contains unique values.
#Since list is an unhashable type for set because it is mutable that’s why first we convert each row (list) into tuple then we put all tuple in set.
#Resultant set will contain only unique valued tuples (row).
#Implementation:


#Python3
# Python program to Print unique rows in a
# given boolean matrix using Set with tuples
 
# Function to print unique rows in a given boolean matrix
 
def uniqueRows(input):
 
    # convert each row (list) into tuple
    # we are mapping tuple function on each row of
    # input matrix
    input = map(tuple, input)
 
    # put all rows in set
    result = set(input)
 
    # print all unique rows
    for row in list(result):
        print (row)
 
# Driver program
if __name__ == "__main__":
    input = [[0, 1, 0, 0, 1],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 0, 1],
            [1, 1, 1, 0, 0]]
    uniqueRows(input)
#Output
#(1, 1, 1, 0, 0)
#(0, 1, 0, 0, 1)
#(1, 0, 1, 1, 0)


