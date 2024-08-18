"""

Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

"""


def longestSubString(s):
    charSet = set()
    left_pointer = 0
    result = 0

    for right_pointer in range(len(s)):
        while s[right_pointer] in charSet:
            charSet.remove(s[left_pointer])
            left_pointer += 1
        charSet.add(s[right_pointer])
        result = max(result, right_pointer - left_pointer + 1)
    return result


longest_substring = longestSubString("abcabcbb")
print(longest_substring)
