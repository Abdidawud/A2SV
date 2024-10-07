# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans=0
        set1=set(allowed)
        for word in words:
            count=0
            for char in set(word):
                if char not in set1:
                    break
                count+=1
            if count ==len(set(word)):
                ans+=1
        return ans