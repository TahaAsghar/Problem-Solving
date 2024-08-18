"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""
from typing import List


def maxProfit(prices):
    left_pointer = 0  # buy stock
    right_pointer = 1  # sell stock
    max_profit = 0
    while right_pointer < len(prices):
        if prices[left_pointer] < prices[right_pointer]:
            profit = prices[right_pointer] - prices[left_pointer]
            max_profit = max(max_profit, profit)
        else:
            left_pointer = right_pointer
        right_pointer += 1

    return max_profit


price = [7, 1, 5, 3, 6, 4]
print(maxProfit(price))
