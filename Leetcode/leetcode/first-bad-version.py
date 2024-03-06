# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i=1
        j=n
        best=n
        while i<=j:
            mid=(j+i)//2
            if not isBadVersion(mid):
                i=mid+1
            else:
                j=mid-1
                best=mid
        return best