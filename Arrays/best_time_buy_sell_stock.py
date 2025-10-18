#time limit exceeded for large data
"""def maxProfit( prices: list[int]) -> int:
    profit=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            temp=prices[j]-prices[i]
            profit=max(profit,temp)
    print(profit)"""
#here is the optimal solution
def maxprofit(prices):
    buy=prices[0]
    profit=0
    for i in range(len(prices)):
        if prices[i]<buy:
            buy=prices[i]
        elif prices[i]-buy>profit:
            profit=prices[i]-buy
    print(profit)

lis=[2,4,1]
maxprofit(lis)

#Kadane's Algorithm
"""Kadane's Algorithm is a dynamic programming technique
 used to find the maximum subarray sum in an array of numbers."""