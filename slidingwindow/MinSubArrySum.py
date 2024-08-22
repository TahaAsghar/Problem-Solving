"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
"""
from typing import List


def minSubArraySum(target: int, nums: List[int]):
    left = 0
    total = 0
    result = float("inf")

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            result = min(result, (right - left + 1))
            total -= nums[left]
            left += 1

    return 0 if result == float("inf") else result


min_sub_sum = minSubArraySum(7, [2, 3, 1, 2, 4, 3])
print(min_sub_sum)
