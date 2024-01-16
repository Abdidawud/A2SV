class Solution:
    def smallestNumber(self, num: int) -> int:
        li = []
        val = abs(num)
        val=str(val)
        li = list(val)
        li.sort(reverse=(num<0))

        if num < 0:
            value  = "".join(li)
            return (-int(value))

        else:
            a = 0
            while a< len(li):
                if li[a] != '0':
                    li[a],li[0] = li[0],li[a]
                    break
                a += 1
            value = "".join(li)
            return ( int(value))