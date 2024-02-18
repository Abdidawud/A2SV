class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        set_=set(fronts+backs)
        for i in range(len(fronts)):
            if fronts[i]==backs[i] and fronts[i] in set_:
                set_.remove(fronts[i])
        
        if len(set_)==0:
            return 0
        else:
            return set_.pop()