class queueObj():
    def __init__(self, maxsize=None):
            self.queue = []
            self.maxsize = maxsize

    def add(self, item):
        if(self.maxsize is None or (len(self.queue) < self.maxsize)):
            self.queue.append(item)
        else:
            raise ValueError("Queue be full")
            
    def FifoGet(self):
        if(len(self.queue) > 0):
            item = self.queue[0]
            self.queue.pop(0)
            return item
        
    def LifoGet(self):
        if(len(self.queue) > 0):
            lastIndex = len(self.queue)-1
            item = self.queue[lastIndex]
            self.queue.pop(lastIndex)
            return item
        
    def queue(self):
        return self.queue
    
    def fullCheck(self):
        if(len(self.queue) < self.maxsize):
            return False
        else:
            return True
    
    def emptyCheck(self):
        if(len(self.queue) > 0):
            return False
        else:
            return True
    
    def swapWithFront(self, index: int):
        if(index > 0 and len(self.queue) >= index):
            store_prev = self.queue[index-1]
            self.queue[index-1] = self.queue[index]
            self.queue[index] = store_prev
        else:
            raise ValueError("No item to swap with")


class priorityQueueObj(queueObj):
    def __init__(self, maxsize=None):
            self.queue = []
            super().__init__(maxsize)

    def add(self, item: any, **kwargs):
        if(len(kwargs) == 1 and kwargs["priorityNum"]):
            priorityNum = kwargs["priorityNum"]
        else:
            priorityNum = len(self.queue)
        
        def _sortQueue(queue):
            for ind, item in enumerate(queue):
                if(ind < len(queue)-1):
                    nextItemPriorityNum = queue[ind+1][0]
                    #if next item higher priority than current
                    if(nextItemPriorityNum < item[0]):
                        storeItem = queue[ind+1]
                        queue[ind+1] = item
                        queue[ind] = storeItem
                        return _sortQueue(queue) #without this, only moves item by one
            
        if(self.maxsize is None or (len(self.queue) < self.maxsize)):
            #given priorityNum cannot be already taken
            if(any(num[0] == priorityNum for num in self.queue)):
                raise ValueError("Priority value already reserved")                
            self.queue.append([priorityNum, item])

            if(len(self.queue) > 1):
                _sortQueue(self.queue)
        else:
            raise ValueError("Queue be full")
    
    def priorityGet(self, priorityNum):
        if(len(self.queue) > 0):
            for item in self.queue:
                if(item[0] == priorityNum):
                    return item[1]
            raise ValueError("Could not find item based on given priorityNum")
        else:
            raise ValueError("Queue has no items")
        
    #priority queue has no reason to have access to this function
    def swapWithFront(self, index: int):
        raise ValueError("Function is restricted to only work with queueObj types")

q = queueObj(maxsize=5)
q2 = priorityQueueObj(maxsize=7)

q2.add(1, priorityNum=7)
q2.add(35, priorityNum=3)
q2.add(3, priorityNum=5)
q2.add(4, priorityNum=4)
q2.add(6, priorityNum=12)
q2.add(219, priorityNum=8)
q2.add(21, priorityNum=2)

print("\nPriority Queue:",q2.queue)

#q2.swapWithFront(4)
#q2.priorityGet(0)
print(f"State of queue post swap: {q2.queue}")
print(f"Priority Queue FIFO and LIFO Gets: FIFO: {q2.FifoGet()}, LIFO: {q2.LifoGet()}, priorityGET: {q2.priorityGet(3)}")
print(f"Final priority queue: {q2.queue}, Full check: {q2.fullCheck()}, Empty check: {q2.emptyCheck()}\n")




q.add("hello")
q.add([])
q.add((1,3,"4"))
q.add("lol")

print("Queue:",q.queue)
q.swapWithFront(2)
q.swapWithFront(1)
print(f"State of queue post swap: {q.queue}")
print(f"Queue FIFO and LIFO Gets: FIFO: {q.FifoGet()}, LIFO: {q.LifoGet()}")

print(f"Final queue: {q.queue}, Full check: {q.fullCheck()}, Empty check: {q.emptyCheck()}\n")