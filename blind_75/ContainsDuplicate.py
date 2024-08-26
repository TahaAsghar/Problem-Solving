"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

 Example 1:

Input: nums = [1,2,3,1]
Output: true
"""
from typing import List


def containsDuplicate(nums: List[int]):
    hash_set = set()

    for n in nums:
        if n in hash_set:
            return True
        hash_set.add(n)
    return False


print(containsDuplicate([1, 2, 3, 1]))
