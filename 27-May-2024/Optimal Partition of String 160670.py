# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        dic=defaultdict(set)
        i=0
        for j in range(len(s)):
            if s[j] in dic[i]:
                i+=1
            dic[i].add(s[j])
        return len(dic)