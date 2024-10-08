# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=[]
        for word in words:
            dic1={}
            dic2={}
            flag=True
            for i in range(len(word)):
                if pattern[i] in dic1:
                    if dic1[pattern[i]]!=word[i]:
                        flag=False
                        break
                elif word[i] in dic2:
                    if dic2[word[i]]!=pattern[i]:
                        flag=False
                        break
                else:
                    dic1[pattern[i]]=word[i]
                    dic2[word[i]]=pattern[i]
            if flag:
                ans.append(word)
        return ans