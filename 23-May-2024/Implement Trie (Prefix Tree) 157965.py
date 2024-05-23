# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
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
        cur=self.root
        for char in word:
            end=cur
            if not cur.children[ord(char)-ord("a")]:
                return False
            cur=cur.children[ord(char)-ord("a")]
        return end.children[ord(word[-1])-ord("a")].is_end

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for char in prefix:
            if not cur.children[ord(char)-ord("a")]:
                return False
            cur=cur.children[ord(char)-ord("a")]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)