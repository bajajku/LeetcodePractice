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

        
class NumberContainers:
    def __init__(self):
        # Map to store number -> min heap of indices
        self.number_to_indices = defaultdict(list)
        # Map to store index -> number
        self.index_to_numbers = {}

    def change(self, index: int, number: int) -> None:
        # Update index to number mapping
        self.index_to_numbers[index] = number

        # Add index to the min heap for this number
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        # If number doesn't exist in our map
        if not self.number_to_indices[number]:
            return -1

        # Keep checking top element until we find valid index
        while self.number_to_indices[number]:
            index = self.number_to_indices[number][0]

            # If index still maps to our target number, return it
            if self.index_to_numbers.get(index) == number:
                return index

            # Otherwise remove this stale index
            heapq.heappop(self.number_to_indices[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
