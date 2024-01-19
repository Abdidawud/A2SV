class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target=skill[0]+skill[-1]

        left=0
        right=len(skill)-1
        ans=[]

        while left < right:
            current_sum=skill[left]+skill[right]
            if current_sum != target:
                return -1
            elif current_sum==target:
                ans.append(skill[left])
                ans.append(skill[right])
            left+=1
            right-=1
             
        i=0
        j=1
        op=0
        while j<=len(ans)-1:
            op+=ans[i]*ans[j]
            i+=2
            j+=2

        return op