class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dic=defaultdict(int)
        my_set={"a","e","i","o","u"}
        op=0

        for i in range(k):
            if s[i] in my_set:
                dic[s[i]]+=1
                op+=1
        right=k
        left=0
        max_=op
        if k==len(s)-1:
            return op
        while right<len(s):
            if s[left] in my_set:
                dic[s[left]]-=1
                op-=1
            if s[right] in my_set:
                dic[s[right]]+=1
                op+=1
            right+=1
            left+=1
            max_=max(max_,op)
        
        return max_