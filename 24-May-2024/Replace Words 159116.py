# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class Solution:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=TrieNode()
            cur=cur.children[char]
        cur.is_end=True
    def find(self,word):
        cur=self.root
        temp=[]
        for char in word:
            if cur.is_end:
                return "".join(temp)
            if char not in cur.children:
                return word
            temp.append(char)
            cur=cur.children[char]
        return word
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        temp=[]
        for word in sentence.split():
            temp.append(self.find(word))
        return " ".join(temp)
