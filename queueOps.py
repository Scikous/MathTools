class QueueObj():
    def __init__(self, maxsize=None):
            self.queue = []
            self.maxsize = maxsize

    def add(self, item):
        if(self.maxsize is None or (len(self.queue) < self.maxsize)):
            self.queue.append(item)
        else:
            raise ValueError("Queue be full")
            
    def get(self):
        if(len(self.queue) > 0):
            item = self.queue[0]
            self.queue.pop(0)
            return item
        
    def lifo_get(self):
        if(len(self.queue) > 0):
            lastIndex = len(self.queue)-1
            item = self.queue[lastIndex]
            self.queue.pop(lastIndex)
            return item
        
    def queue(self):
        return self.queue
    
    def is_full(self):
        if(len(self.queue) < self.maxsize):
            return False
        else:
            return True
    
    def is_empty(self):
        if(len(self.queue) > 0):
            return False
        else:
            return True
    
class LifoQueueObj(QueueObj):
    def __init__(self, maxsize=None):
            self.queue = []
            super().__init__(maxsize)

    def get(self):
        if(len(self.queue) > 0):
            lastIndex = len(self.queue)-1
            item = self.queue[lastIndex]
            self.queue.pop(lastIndex)
            return item

class PriorityQueueObj(QueueObj):
    def __init__(self, maxsize=None):
            self.queue = []
            super().__init__(maxsize)

    def add(self, item, priority_num=None):
        if not priority_num:
            priority_num = len(self.queue)
        
        def _sortQueue(queue):
                lower_priorities = []
                higher_priorities = []

                while queue:#empty out queue while storing values
                    #newest value gets sorted automatically
                    if queue[0][0] > priority_num :#store lower priority values
                        lower_priorities.append(queue[0])
                    else:#store higher priority values
                        higher_priorities.append(queue[0])
                    queue.pop(0)
                while higher_priorities:#add back the highest priority values
                    queue.append(higher_priorities[0])
                    higher_priorities.pop(0)
                while lower_priorities:#add back the lowest priority values
                    queue.append(lower_priorities[0])
                    lower_priorities.pop(0)
            
        if(self.maxsize is None or (len(self.queue) < self.maxsize)):
            #given priority_num cannot be already taken
            if(any(num[0] == priority_num for num in self.queue)):
                raise ValueError("Priority value already reserved")               
            self.queue.append((priority_num, item))

            if(len(self.queue) > 1):
                _sortQueue(self.queue)
        else:
            raise ValueError("Queue be full")
    
    def get(self, priority_num=None):
        if len(self.queue) > 0:
            items_tmp = []
            if not priority_num: #return highest priority value (already sorted)
                item = self.queue[0]
                self.queue.pop(0)
            else:
                while self.queue:#find elem based on priority number
                    item = self.queue[0]
                    if priority_num == item[0]:
                        break
                    items_tmp.append(item)
                    self.queue.pop(0)
                
                while items_tmp:#re-insert values back to queue
                    item_tmp, priority = items_tmp[0]
                    self.add(item_tmp,priority_num=priority)
                    items_tmp.pop(0)

            return item[1]
        else:
            raise ValueError("Queue has no items")
  
def swap_with_front(normal_queue, n: int):
    if(n > 0):
        ind = 0
        queue_items = []
        item = None
        while normal_queue.queue:
            if ind == n-1:
                item = normal_queue.queue[0]
                normal_queue.queue.pop(0)
                ind += 1

            queue_items.append(normal_queue.queue[0])
            if item is not None:
                queue_items.append(item)
                item = None
            normal_queue.queue.pop(0)
            ind += 1

        while queue_items:
            normal_queue.add(queue_items[0])
            queue_items.pop(0)
        return normal_queue
    else:
        raise ValueError("No item to swap with")

def lifo_fifo_queue_print(inp_queue):
    print("Queue:",inp_queue.queue)
    swap_with_front(inp_queue, 2)
    swap_with_front(inp_queue, 1)
    print(f"State of queue post swap: {inp_queue.queue}")
    print(f"Queue get: {inp_queue.get()}")
    print(f"Queue: {inp_queue.queue}, Full check: {inp_queue.is_full()}, Empty check: {inp_queue.is_empty()}")

    while not inp_queue.is_full():
        inp_queue.add(([],{},[1,2,4,"5"],"pp"))
    print(f"Filled up queue: {inp_queue.queue},\nQueue Full Check: {inp_queue.is_full()}, Empty Check: {inp_queue.is_empty()}")
    while not inp_queue.is_empty():
        inp_queue.get()
    print(f"State of queue post emptying: {inp_queue.queue}, Full check: {inp_queue.is_full()}, Empty check: {inp_queue.is_empty()}")


if __name__ == '__main__':
    #FIFO queue
    fifo_queue = QueueObj(maxsize=5)

    fifo_queue.add("hello")
    fifo_queue.add([])
    fifo_queue.add((1,3,"4"))
    fifo_queue.add("lol")

    print("FIFO queue:")
    lifo_fifo_queue_print(fifo_queue)
    print("\n")

    #LIFO queue
    lifo_queue = LifoQueueObj(maxsize=7)

    lifo_queue.add({})
    lifo_queue.add([{}])
    lifo_queue.add((6,[],"4", {}))
    lifo_queue.add("wau")

    print("LIFO queue:")
    lifo_fifo_queue_print(lifo_queue)

    #priority queue
    priority_queue = PriorityQueueObj(maxsize=7)

    priority_queue.add(1, priority_num=7)
    priority_queue.add(35, priority_num=3)
    priority_queue.add(3, priority_num=5)
    priority_queue.add(4, priority_num=4)
    priority_queue.add(6, priority_num=12)
    priority_queue.add(219, priority_num=8)
    #priority_queue.add(219, priority_num=8)
    priority_queue.add(21, priority_num=2)
    print(f"Full check: {priority_queue.is_full()}")

    print("\nPriority Queue:",priority_queue.queue)
    print(f"Priority Queue get: Highest Priority: {priority_queue.get()}, Specific Priority (7): {priority_queue.get(7)}")
    print(f"Final priority queue: {priority_queue.queue}, Full check: {priority_queue.is_full()}, Empty check: {priority_queue.is_empty()}")
    
    while not priority_queue.is_empty():
        priority_queue.get()
    print(f"Empty priority queue: {priority_queue}, Full check: {priority_queue.is_full()}, Empty check: {priority_queue.is_empty()}\n")
    