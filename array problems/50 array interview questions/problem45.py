#Stock Buy Sell to Maximize Profit

#Difficulty Level : Medium

#----------------------------------------------------------------------------
#The cost of a stock on each day is given in an array. Find the maximum profit that you can make by buying and selling on those days. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

#Examples:

#Input: arr[] = {100, 180, 260, 310, 40, 535, 695}
#Output: 865
#Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210
#                       Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655
#                       Maximum Profit  = 210 + 655 = 865

#Input: arr[] = {4, 2, 2, 2, 4}
#Output: 2
#Explanation: Buy the stock on day 1 and sell it on day 4 => 4 – 2 = 2
#                       Maximum Profit  = 2
#---------------------------------------------------------------------
#A simple approach is to try buying the stocks and selling them every single day when profitable and keep updating the maximum profit so far.

#Follow the steps below to solve the problem:

#Try to buy every stock from start to end – 1
#After that again call the maxProfit function to calculate answer
#curr_profit = price[j] – price[i] + maxProfit(start, i – 1) + maxProfit(j + 1, end)
#profit = max(profit, curr_profit)
#Below is the implementation of the above approach:




# Python3 implementation of the approach
  
# Function to return the maximum profit
# that can be made after buying and
# selling the given stocks
  
  
def maxProfit(price, start, end):
  
    # If the stocks can't be bought
    if (end <= start):
        return 0
  
    # Initialise the profit
    profit = 0
  
    # The day at which the stock
    # must be bought
    for i in range(start, end, 1):
  
        # The day at which the
        # stock must be sold
        for j in range(i+1, end+1):
  
            # If buying the stock at ith day and
            # selling it at jth day is profitable
            if (price[j] > price[i]):
  
                # Update the current profit
                curr_profit = price[j] - price[i] +\
                    maxProfit(price, start, i - 1) + \
                    maxProfit(price, j + 1, end)
  
                # Update the maximum profit so far
                profit = max(profit, curr_profit)
  
    return profit
  
  
# Driver code
if __name__ == '__main__':
    price = [100, 180, 260, 310, 40, 535, 695]
    n = len(price)
  
    print(maxProfit(price, 0, n - 1))
  
# This code is contributed by Rajput-Ji
#Output
#865
#Time Complexity: O(N2), Trying to buy every stock and exploring all possibilities.
#Auxiliary Space: O(1)
#----------------------------------------------------
#Stock Buy Sell to Maximize Profit using Local Maximum and Local Minimum:
#If we are allowed to buy and sell only once, then we can use the algorithm discussed in maximum difference between two elements. Here we are allowed to buy and sell multiple times. 

#Follow the steps below to solve the problem:  

#Find the local minima and store it as starting index. If it does not exists, return.
#Find the local maxima. And store it as an ending index. If we reach the end, set the end as the ending index.
#Update the solution (Increment count of buy-sell pairs)
#Repeat the above steps if the end is not reached.
#Below is the implementation of the above approach:


# Python3 Program to find
# best buying and selling days
  
# This function finds the buy sell
# schedule for maximum profit
  
  
def stockBuySell(price, n):
  
    # Prices must be given for at least two days
    if (n == 1):
        return
  
    # Traverse through given price array
    i = 0
    while (i < (n - 1)):
  
        # Find Local Minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
        while ((i < (n - 1)) and
                (price[i + 1] <= price[i])):
            i += 1
  
        # If we reached the end, break
        # as no further solution possible
        if (i == n - 1):
            break
  
        # Store the index of minima
        buy = i
        i += 1
  
        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1
  
        # Store the index of maxima
        sell = i - 1
  
        print("Buy on day: ", buy, "\t",
              "Sell on day: ", sell)
  
# Driver code
  
  
# Stock prices on consecutive days
price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)
  
# Function call
stockBuySell(price, n)
  
# This is code contributed by SHUBHAMSINGH10
#Output
#Buy on day: 0     Sell on day: 3
#Buy on day: 4     Sell on day: 6
#Time Complexity:  O(N), The outer loop runs till I become n-1. The inner two loops increment the value of I in every iteration.
#Auxiliary Space: O(1)
#---------------------------------------------------------------------


#Stock Buy Sell to Maximize Profit using Valley Peak Approach:
#In this approach, we just need to find the next greater element and subtract it from the current element so that the difference keeps increasing until we reach a minimum. If the sequence is a decreasing sequence, so the maximum profit possible is 0.

#Follow the steps below to solve the problem:

maxProfit = 0
#if price[i] > price[i – 1]
#maxProfit = maxProfit + price[i] – price[i – 1]
#Below is the implementation of the above approach:


# Python3 program for the above approach
def max_profit(prices: list, days: int) -> int:
  
    profit = 0
  
    for i in range(1, days):
  
        # checks if elements are adjacent and in increasing order
        if prices[i] > prices[i-1]:
  
            # difference added to 'profit'
            profit += prices[i] - prices[i-1]
  
    return profit
  
  
# Driver Code
if __name__ == '__main__':
  
    # stock prices on consecutive days
    prices = [100, 180, 260, 310, 40, 535, 695]
  
    # function call
    profit = max_profit(prices, len(prices))
    print(profit)
  
    # This code is contributed by vishvofficial.
#Output
#865
#Time Complexity: O(N), Traversing over the array of size N.
#Auxiliary Space: O(1)