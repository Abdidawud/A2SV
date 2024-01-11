class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common=[]
        set1=set(nums1)
        set2=set(nums2)

        common=list(set1.intersection(set2))

        if common==[]:
            return -1
        else:
            return min(common)