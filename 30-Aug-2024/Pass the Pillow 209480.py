# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur_pos=1
        cur_time=0
        dire=1

        while cur_time<time:
            if 0<cur_pos+dire<=n:
                cur_pos+=dire
                cur_time+=1
            else:
                dire*=-1
        return cur_pos