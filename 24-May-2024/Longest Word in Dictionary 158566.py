# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TriNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TriNode()
        def insert(word):
            tri = root
            for i in word:
                cur_ind = ord(i)-ord("a")
                if not tri.children[cur_ind]:
                    tri.children[cur_ind] = TriNode()
                tri = tri.children[cur_ind]
            tri.is_end= True
        for word in words:
            insert(word)
        res = defaultdict(list)
        def dfs(root,arr):
            for child in root.children:
                if child and child.is_end:
                    break
            else:
                res[len(arr)].append("".join(arr))
                return 
            ls = arr
            for i in range(26):
                if root.children[i] and root.is_end:
                    ls.append(chr(i+ord("a")))
                    dfs(root.children[i],ls)
                    ls.pop()
            return ls
        for i in range(26):
            if root.children[i] and root.children[i].is_end:
                dfs(root.children[i],[chr(i+ord("a"))])

        return sorted(res[max(res.keys())])[0] if res else ""
