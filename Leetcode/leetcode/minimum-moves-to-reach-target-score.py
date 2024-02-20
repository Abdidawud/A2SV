class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans=0
        
        if maxDoubles>0:
            for i in range(maxDoubles):
                if target==1:
                    break
                if target %2 != 0:
                    ans+=2
                    target=target//2
                else:
                    ans+=1
                    target =target/2
                print (target)
            if target>1:
                ans+=target-1
        else:
            ans=target-1
        return int(ans)