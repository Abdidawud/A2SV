class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        z=''.join(word1)
        y=''.join(word2)
        if z==y:
            return True
        else:
            return False