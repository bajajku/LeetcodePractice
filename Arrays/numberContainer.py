class NumberContainers:

    def __init__(self):
        self.map = {}
        self.numIndex = collections.defaultdict(SortedSet)
        

    def change(self, index: int, number: int) -> None:

        if(index in self.map):
            prev = self.map[index]
            self.numIndex[prev].remove(index)

            if(not self.numIndex[prev]):
                del self.numIndex[prev]
        self.map[index] = number
        self.numIndex[number].add(index)

    def find(self, number: int) -> int:

        if(number in self.numIndex):
            return self.numIndex[number][0]
        
        return -1

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
