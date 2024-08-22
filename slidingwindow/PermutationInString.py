"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""


def checkPermutations(s1: str, s2: str):
    if len(s1) > len(s2): return False
    countS1 = [0] * 26
    countS2 = [0] * 26

    for i in range(len(s1)):
        countS1[ord(s1[i]) - ord('a')] += 1
        countS2[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        matches += (1 if countS1[i] == countS2[i] else 0)

    left = 0
    for right in range(len(s1), len(s2)):
        if matches == 26: return True

        index = ord(s2[right]) - ord('a')
        countS2[index] += 1

        if countS1[index] == countS2[index]:
            matches += 1
        elif countS1[index] + 1 == countS2[index]:
            matches -= 1

        index = ord(s2[left]) - ord('a')
        countS2[index] -= 1

        if countS1[index] == countS2[index]:
            matches += 1
        elif countS1[index] - 1 == countS2[index]:
            matches -= 1
        left += 1

    return matches == 26


permutations = checkPermutations("ab", "eidbaooo")
print(permutations)
