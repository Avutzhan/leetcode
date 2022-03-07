class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None for i in range(n + 1)]
        self.index = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.arr[id - 1] = value
        result = []
        while self.arr[self.index] != None:
            result.append(self.arr[self.index])
            self.index += 1
        return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
# param_2 = obj.insert(id,value)
# param_3 = obj.insert(id,value)

# причина добавления доп элемента в начальный массив то что в питоне не доступно динамическое
# добавление элементов и питон возвращает ошибку но php js просто спокойно добавляют новый элемент
