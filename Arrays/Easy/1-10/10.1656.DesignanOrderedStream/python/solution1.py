class OrderedStream:

    stream = [] #you can omit this
    temp = 0 #you can omit this

    def __init__(self, n: int):
        self.stream = [None for i in range(n + 1)]
        self.temp = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id - 1] = value
        ans = []
        while self.stream[self.temp] != None:
            ans.append(self.stream[self.temp])
            self.temp+=1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)