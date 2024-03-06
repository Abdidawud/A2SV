class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target<letters[0]:
            return letters[0]
        left=0
        right=len(letters)-1
        min_='#'
        while left<=right:
            mid=(right+left)//2
            if target==letters[mid]:
                left=mid+1
            elif target>letters[mid]:
                left=mid+1
            else:
                right=mid-1
                min_=letters[mid]
        if min_=='#':
            return letters[0]
        return min_