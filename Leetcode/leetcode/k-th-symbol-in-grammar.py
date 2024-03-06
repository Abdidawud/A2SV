class Solution:
    def __init__(self):
        self.result=0
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return int(self.result)
        
        middle=2**(n-2)
        if k>middle:
            k-=middle
            self.result=not self.result
        return self.kthGrammar(n-1,k)
    

        