# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        z=''.join(word1)
        y=''.join(word2)
        if z==y:
            return True
        else:
            return False