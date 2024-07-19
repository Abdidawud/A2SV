# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count=0
        new_arr=[x-y for x,y in zip(nums1,nums2)]
        
        print(new_arr)
        def counting(left_half,right_half):
            nonlocal count
            l=0
            r=0
            while l<len(left_half)and r<len(right_half):
                if left_half[l]<=right_half[r]+diff:
                    count+=len(right_half)-r
                    l+=1
                else:
                    r+=1
            return
                
        def merge(left_half,right_half):
            nonlocal count
            l=0
            r=0
            res=[]
            while l<len(left_half) and r<len(right_half):
                if left_half[l]<=right_half[r]:
                    res.append(left_half[l])
                    l+=1
                else:
                    res.append(right_half[r])
                    r+=1
            res.extend(left_half[l:])
            res.extend(right_half[r:])
            return res
        def mergesort(left,right,arr):
            if left==right:
                return [arr[left]]
            mid=left+(right-left)//2
            left_half=mergesort(left,mid,arr)
            right_half=mergesort(mid+1,right,arr)
            
            counting(left_half,right_half)
            return merge(left_half,right_half)
        
        mergesort(0,len(new_arr)-1,new_arr)
        return count