class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic=defaultdict(int)
        min_=float('inf')
        left=0
        right=0
        flag=False
    
        while right<len(cards):
            dic[cards[right]] +=1

            if dic[cards[right]]>=2:
                flag=True
                while cards[left] != cards[right]:
                    dic[cards[left]]-=1
                    left+=1
                min_=min(min_,(right-left))
                dic [cards[left]]-=1
                left+=1
                right+=1
            else:
                right+=1
        return (min_+1) if min_ != float("inf") else -1