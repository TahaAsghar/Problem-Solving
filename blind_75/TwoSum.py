"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""
from typing import List


def two_sum(nums: List[int], target: int):
    numsMap = {}

    for i, n in enumerate(nums):
        difference = target - n
        if difference in numsMap:
            return [numsMap[difference], i]
        numsMap[n] = i


print(two_sum([2, 7, 11, 15], 9))
