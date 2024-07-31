# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        i =0
        j = 0
        dic = defaultdict(int)

        while j < len(fruits):
            dic[fruits[j]]+=1
            while len(dic) > 2:
                dic[fruits[i]] -= 1
                if dic[fruits[i]] == 0:
                    dic.pop(fruits[i])
                i+=1
            j+=1
            ans = max(ans, j-i)
        return ans