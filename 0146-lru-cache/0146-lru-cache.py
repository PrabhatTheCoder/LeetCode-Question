class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.cap = capacity

        # Dummy head and tail
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, delnode):
        prevv = delnode.prev
        nextt = delnode.next
        prevv.next = nextt
        nextt.prev = prevv

    def addNode(self, newnode):
        temp = self.head.next
        newnode.next = temp
        newnode.prev = self.head
        self.head.next = newnode
        temp.prev = newnode
        
    def get(self, key: int) -> int:
        if key in self.dic:
            resNode = self.dic[key]
            ans = resNode.value

            # Make it recently used
            self.deleteNode(resNode)
            self.addNode(resNode)

            self.dic[key] = self.head.next
            return ans

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            curr = self.dic[key]
            del self.dic[key]
            self.deleteNode(curr)

        # If capacity is full, remove LRU
        if len(self.dic) == self.cap:
            lru = self.tail.prev
            del self.dic[lru.key]
            self.deleteNode(lru)

        newnode = ListNode(key, value)
        self.addNode(newnode)
        self.dic[key] = self.head.next
