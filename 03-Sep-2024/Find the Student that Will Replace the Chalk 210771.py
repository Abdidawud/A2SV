# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_=sum(chalk)
        val=k%sum_
        i=0
        while val>0:
            if val-chalk[i]>=0:
                val-=chalk[i]
                i+=1
            else:
                break
        return i