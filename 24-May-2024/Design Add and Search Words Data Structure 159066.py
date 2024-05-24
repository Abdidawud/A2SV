# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word: str) -> None:
        cur=self.root
        for char in word:
            end=cur
            if not cur.children[ord(char)-ord('a')]:
                new=TrieNode()
                cur.children[ord(char)-ord('a')]=new
                cur=new
            else:
                cur=cur.children[ord(char)-ord('a')]
        end.children[ord(word[-1])-ord('a')].is_end=True

    def search(self, word: str) -> bool:
        def dfs(index,root):
            cur=root
            for i in range(index,len(word)):
                temp=word[i]
                if temp==".":
                    for child in cur.children:
                        if child and dfs(i+1,child):
                            return True
                    return False
                else:
                    index=ord(temp)-ord("a")
                    if not cur.children[index]:
                        return False
                    cur=cur.children[index]
            return cur.is_end
        return dfs(0,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)