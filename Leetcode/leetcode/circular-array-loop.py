class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        past=set()
        n=len(nums)

        for i in range(n):
            if i not in past:
                now=set()
                while True:
                    if i in now:
                        return True
                    now.add(i)
                    past.add(i)
                    
                    j=i
                    i=(i +nums[i])%n

                    if nums[j] >=0 !=nums[i]<0:
                        break
                    if j==i:
                        break
        return False