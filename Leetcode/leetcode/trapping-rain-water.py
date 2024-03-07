class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=[]
        max_right=[]
        max_=0
        for i in range(len(height)):
            max_left.append(max_)
            max_=max(max_,height[i])
            
        max_=0
        for i in range(len(height)-1,-1,-1):
            max_right.insert(0,max_)
            max_=max(max_,height[i])
            
        ans=0
        for i in range(len(height)):
            temp=(min(max_left[i],max_right[i]))-height[i]
            if temp>=0:
                ans+=temp
        return ans