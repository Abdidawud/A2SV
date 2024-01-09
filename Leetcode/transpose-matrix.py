class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[i for i in zip(*matrix)]
        return ans