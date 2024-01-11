class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        dic=Counter(nums1)
        for i in nums2:
            
            if dic[i]>0:
                ans.append(i)
                dic[i]-=1
        
        return ans