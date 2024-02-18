class OrderedStream:

    def __init__(self, n: int):
        self.dic={}
        self.count=1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.dic[idKey]=value
        li=[]
        i=self.count
        
        while i in self.dic:
            li.append(self.dic[i])
            i+=1
        self.count=i
        return li

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)