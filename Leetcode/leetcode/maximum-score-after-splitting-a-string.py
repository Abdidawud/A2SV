class Solution:
    def maxScore(self, s: str) -> int:
        acc=0
        prefix_sum=[]
        for i in range(len(s)):
            acc+=int(s[i])
            prefix_sum.append(acc)
        acc=0
        postfix_sum=[]
        for i in range(len(s)-1,-1,-1):
            acc+=int(s[i])
            postfix_sum.append(acc)
        
        postfix_sum=postfix_sum[::-1]
        max_=0
        
        for i in range(len(s)-1):
            left=(i+1)-prefix_sum[i]
            right=postfix_sum[i+1]
            max_=max(max_,right+left)
        
        return max_