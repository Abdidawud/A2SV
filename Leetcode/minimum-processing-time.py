class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()

        ans=0
        i=0
        j=3
        while i < len(processorTime):
            c=processorTime[i]+tasks[j]
            print(c)
            ans=max(ans,c)
            i+=1
            j+=4
        
        return ans