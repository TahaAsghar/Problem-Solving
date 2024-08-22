"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings)
that occur more than once in a DNA molecule. You may return the answer in any order.


Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
"""


def repeatedDnaSequence(s: str):
    result = set()
    seen = set()

    for left in range(len(s) - 9):
        cur = s[left:left + 10]
        if cur in seen:
            result.add(cur)
        seen.add(cur)
    return list(result)


dna_sequence = repeatedDnaSequence("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print(dna_sequence)
