"""
The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k.
In one operation, you can choose an index of nums and increment the element at that index by 1.
Return the maximum possible frequency of an element after performing at most k operations.

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
"""
from typing import List


def maxFrequency(nums: List[int], k: int):
    nums.sort()
    left = 0
    right = 0
    result = 0
    sum_current_window = 0

    while right < len(nums):
        sum_current_window += nums[right]

        while nums[right] * (right - left + 1) > sum_current_window + k:
            sum_current_window -= nums[left]
            left += 1

        result = max(result, right - left + 1)
        right += 1

    return result


max_frequency = maxFrequency([1, 4, 8, 13], 5)
print(max_frequency)
