"""
You are given an array of integers nums,
there is a sliding window of size k which is moving from the very left
of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
"""
import collections
from typing import List


def maxSlidingWindow(nums: List[int], k: int):
    # result = []
    # # left and right represent the window
    # left = 0
    # right = 0
    # q = collections.deque()
    #
    # while right < len(nums):
    #     # popping the smaller value from the queue
    #     while q and nums[q[-1]] < nums[right]:
    #         q.pop()
    #     q.append(right)
    #
    #     # removing the left value from the window
    #     if left > q[0]:
    #         q.popleft()
    #
    #     if (right + 1) >= k:
    #         result.append(nums[q[0]])
    #         left += 1
    #     right += 1
    # return result

    result = []
    q = collections.deque()  # Store indices of the elements

    for i in range(len(nums)):
        # Remove elements not within the sliding window
        if q and q[0] < i - k + 1:
            q.popleft()

        # Remove elements from the deque that are smaller than the current element
        while q and nums[q[-1]] < nums[i]:
            q.pop()

        # Add the current element's index to the deque
        q.append(i)

        # Append the maximum value in the current sliding window to the result list
        if i >= k - 1:
            result.append(nums[q[0]])

    return result


maxWindowValue = maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(maxWindowValue)
