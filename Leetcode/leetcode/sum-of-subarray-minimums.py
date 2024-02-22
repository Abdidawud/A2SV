class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        stack = []
        mod = 10**9 + 7

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                ans = (ans + arr[j] * left * right) % mod
            stack.append(i)

        while stack:
            j = stack.pop()
            left = j - stack[-1] if stack else j + 1
            right = len(arr) - j
            ans = (ans + arr[j] * left * right) % mod

        return ans
