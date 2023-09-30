
import numpy as np
import queue

class queueObj():
    def __init__(self, maxsize=None):
            self.queue = []
            self.maxsize = maxsize
    
    def add(self, item: any):
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





q = queueObj(maxsize=3)
q.add(1)
q.add("hello")
q.add([])
#q.add((1,3,"4"))

print("Queue:",q.queue)
q.swapWithFront(2)
q.swapWithFront(1)
print(f"State of queue post swap: {q.queue}")
print(f"Queue FIFO and LIFO Gets: FIFO: {q.FifoGet()}, LIFO: {q.LifoGet()}")

print(q.queue, q.fullCheck(), q.emptyCheck())

q2 = queue.Queue()
print(q2.queue)
print(q2.full())
q2.put(1)
q2.put(2)
q2.put(3)
q2.empty()

print(q2.empty())
# q.get()
# print(q.queue)
