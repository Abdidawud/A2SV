class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue=deque([i,t] for i,t in enumerate(tickets))
        n=len(tickets)
        ans=0

        while queue:
            idx,num_ticket=queue.popleft()
            ans+=1

            if num_ticket >1:
                queue.append([idx,num_ticket-1])
            if idx==k and num_ticket==1:
                return ans
        return ans