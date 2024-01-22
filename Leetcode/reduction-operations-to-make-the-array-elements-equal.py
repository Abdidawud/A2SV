class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0

        nu=list(set(nums))
        nu.sort(reverse=True)
        
        for i in range(len(nu)-1):
            ans+=count[nu[i]]
            count[nu[i+1]]+=count[nu[i]]
        
        return ans