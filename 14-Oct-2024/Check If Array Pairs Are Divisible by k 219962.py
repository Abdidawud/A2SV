# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem_freq=[0]*k
        for i in arr:
            rem=i%k
            rem_freq[rem]+=1
        
        for i in range(k):
            if i==0:
                if rem_freq[i]%2!=0:
                    return False
            
            elif rem_freq[i] != rem_freq[k-i]:
                    return False
        return True