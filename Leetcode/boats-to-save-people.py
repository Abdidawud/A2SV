class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left=0
        right=len(people)-1
        ans=0

        if len(people)==1:
            return 1

        while right>=left:
            if people[left] + people[right] <= limit:
                ans+=1
                left+=1
                right-=1
            elif people[right] <= limit:
                ans+=1
                right-=1
        
        return ans