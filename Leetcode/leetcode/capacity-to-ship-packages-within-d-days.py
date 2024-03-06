class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        best=-1
        
        while low<=high:
            mid=(high+low)//2
            calculated_days=1
            counter=0
            for i in range(len(weights)):
                counter+=weights[i]
                if counter >mid:
                    calculated_days+=1
                    counter=weights[i]
            
            if calculated_days>days:
                low=mid+1
            else:
                high=mid-1
                best=mid
        return best