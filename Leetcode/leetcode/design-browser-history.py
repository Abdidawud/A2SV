class BrowserHistory:

    def __init__(self, homepage: str):
        self.position=0
        self.list=[homepage]

    def visit(self, url: str) -> None:
        if self.position<len(self.list)-1:
            self.list=self.list[:self.position+1]
        self.list.append(url)
        self.position+=1

    def back(self, steps: int) -> str:
        if self.position<steps:
            self.position=0
            return self.list[0]
        else:
            self.position-=steps
            return self.list[self.position]
    def forward(self, steps: int) -> str:
        if len(self.list)-self.position-1<steps:
            self.position=len(self.list)-1
            return self.list[-1]
        else:
            self.position +=steps
            return self.list[self.position]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)