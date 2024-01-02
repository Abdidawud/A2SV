class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for lst in image:
            lst.reverse()
        img = []
        for i in image:
            lst = []
            for j in i:
                if j == 0:
                    lst.append(1)
                else:
                    lst.append(0)
            img.append(lst)
        return img