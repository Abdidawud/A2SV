# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans=0
        now_capacity=capacity
        for i in range(len(plants)):
            if plants[i]>now_capacity:
                ans+= (i)*2 +1
                now_capacity=capacity-plants[i]
                continue
            now_capacity-=plants[i]
            ans+=1
        return ansclass Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans=0
        now_capacity=capacity
        for i in range(len(plants)):
            if plants[i]>now_capacity:
                ans+= (i)*2 +1
                now_capacity=capacity-plants[i]
                continue
            now_capacity-=plants[i]
            ans+=1
        return ans