class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q=deque()
        min_q=deque()
        left=0
        ans=0

        for i, num in enumerate (nums):
            while max_q and num>max_q[-1]:
                max_q.pop()
            while min_q and num<min_q[-1]:
                min_q.pop()
            max_q.append(num)
            min_q.append(num)

            while max_q[0] -min_q[0]>limit:
                if max_q[0]==nums[left]:
                    max_q.popleft()
                if min_q[0]==nums[left]:
                    min_q.popleft()
                left+=1
            ans=max(ans,(i-left+1))
        return ans
            
            