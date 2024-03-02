class Solution:
    def balancedString(self, s: str) -> int:
        def helper(dic,n):
            for key,value in dic.items():
                if max(dic.values())> n:
                    return False
                
                return True
        dic=Counter(s)
        n=len(s)//4
        left=0
        right=0
        ans=float('inf')

        if helper(dic,n):
            return 0
        
        while( right< len(s)):
            dic[s[right]] -=1
            right+=1

            while(helper(dic,n) and left<len(s)):
                ans=min(ans,(right-left))
               
                dic[s[left]]+=1
                left+=1
        return ans