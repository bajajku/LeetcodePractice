class DLL_Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {}
        self.capacity = capacity

        self.head = DLL_Node(-1, -1)
        self.tail = DLL_Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if(key in self.hashMap):
            node = self.hashMap[key]
            
            # removing the node
            prevNode, nextNode = node.prev, node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode

            # inserting the node in front
            headNext = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = headNext  # Add this line to fix the bug
            headNext.prev = node

            return self.hashMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if(key in self.hashMap):
            node = self.hashMap[key]
            
            # removing the node
            prevNode, nextNode = node.prev, node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode

        #update the hashMap
        self.hashMap[key] = DLL_Node(key, value)
        node = self.hashMap[key]
        # inserting the node in front
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext  # Add this line to fix the bug
        headNext.prev = node

        if(len(self.hashMap) > self.capacity):
            LRU_Node = self.tail.prev
            temp = LRU_Node.prev
            temp.next = self.tail
            self.tail.prev = temp

            del self.hashMap[LRU_Node.key]





        
