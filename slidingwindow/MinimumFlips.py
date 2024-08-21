"""
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.
For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
"""


def minFlips(s: str):
    n = len(s)
    s = s + s
    alt1, alt2 = "", ""

    for i in range(len(s)):
        alt1 += "0" if i % 2 else "1"
        alt2 += "1" if i % 2 else "0"

    result = len(s)
    dif1, dif2 = 0, 0
    left = 0

    for right in range(len(s)):
        if s[right] != alt1[right]:
            dif1 += 1
        if s[right] != alt2[right]:
            dif2 += 1

        if (right - left + 1) > n:
            if s[left] != alt1[left]:
                dif1 -= 1
            if s[left] != alt2[left]:
                dif2 -= 1
            left += 1

        if (right - left + 1) == n:
            result = min(result, dif1, dif2)
    return result


min_flips = minFlips("111000")
print(min_flips)
