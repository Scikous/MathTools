class QueueObj():#standard FIFO queue (retrieve first object in queue)
    def __init__(self, maxsize=None):
            self.queue = []
            self.maxsize = maxsize

    def add(self, item):#add to end of queue
        if(self.maxsize is None or (len(self.queue) < self.maxsize)):
            self.queue.append(item)
        else:
            raise ValueError("Queue be full")
            
    def get(self):#FIFO get from queue
        if(len(self.queue) > 0):
            item = self.queue[0]
            self.queue.pop(0)
            return item
        
    def queue(self):#for viewing the entire queue
        return self.queue
    
    def is_full(self):#useful for figuring out if queue is full without raising errors
        if(self.maxsize is not None and len(self.queue) < self.maxsize):
            return False
        else:
            return True
    
    def is_empty(self):#useful for figuring out if queue is empty without raising errors
        if(len(self.queue) > 0):
            return False
        else:
            return True
    
class LifoQueueObj(QueueObj):#LIFO queue, inherits standard queue's methods (retrieves queue's last object first)
    def __init__(self, maxsize=None):
            super().__init__(maxsize)#initialize QueueObj and receive access to methods

    def get(self):#override QueueObj's get method to change it from FIFO to LIFO instead
        if(len(self.queue) > 0):
            item = self.queue[-1]
            self.queue.pop(-1)
            return item

class PriorityQueueObj(QueueObj):#inherits standard queue's methods (retrieves obj based on highest/desired priority)
    def __init__(self, maxsize=None):
        super().__init__(maxsize)#initialize QueueObj

    def add(self, item, priority_num=None):#override QueueObj's add to be priority oriented
        def _next_available_priority_num(q):#find highest available priority number
            priority_num = 0
            while q:
                if priority_num < q[0][1]:
                    priority_num = q[0][1] + 1
                q.pop(0)
            return priority_num
        def _sort_queue():#sort queue from highest to lowest priorities
                lower_priorities = []
                higher_priorities = []

                while self.queue:#empty out queue while storing values
                    #newest value gets sorted automatically
                    if self.queue[0][1] > priority_num :#store lower priority values
                        lower_priorities.append(self.queue[0])
                    else:#store higher priority values
                        higher_priorities.append(self.queue[0])
                    self.queue.pop(0)
                while higher_priorities:#add back the highest priority values
                    self.queue.append(higher_priorities[0])
                    higher_priorities.pop(0)
                while lower_priorities:#add back the lowest priority values
                    self.queue.append(lower_priorities[0])
                    lower_priorities.pop(0)
        if(self.maxsize is None or (len(self.queue) < self.maxsize)):#either queue has no size limit or limit has yet to be reached
            if priority_num is None:
                if self.queue:
                    priority_num = _next_available_priority_num(self.queue.copy())#put behind lowest priority
                else:
                    priority_num = 0
            elif(any(num[1] == priority_num for num in self.queue)):#if priority num is given, it cannot already be taken 
                raise ValueError(f"Priority value '{priority_num}' already reserved")    
            self.queue.append((item, priority_num))

            if(len(self.queue) > 1):#no point in sorting a single item
                _sort_queue()
        else:
            raise ValueError("Queue be full")
    
    def get(self, priority_num=None):#override QueueObj's FIFO get, to get either highest priority or based on given priority
        if len(self.queue) > 0:
            if not priority_num: #return highest priority value (already sorted)
                item = self.queue[0]
                self.queue.pop(0)
            else:
                items_tmp = []
                while self.queue:#find item based on priority number
                    item = self.queue[0]
                    if priority_num == item[1]:
                        break
                    items_tmp.append(item)
                    self.queue.pop(0)
                
                while items_tmp:#re-insert values back to queue
                    item_tmp, priority = items_tmp[0]
                    self.add(item_tmp,priority_num=priority)
                    items_tmp.pop(0)
                    
            return item[0]
        else:
            raise ValueError("Queue has no items")
  
def swap_with_front(J, n: int):#swap n and n-1 values
    if(n > 0):
        ind = 0
        q_items = []
        item = None
        while J.queue:
            if ind == n-1:#if 1 away from nth item, then store it
                item = J.queue[0]
                J.queue.pop(0)
                ind += 1
            q_items.append(J.queue[0])
            if item is not None:#after nth item is added, then add n-1 back
                q_items.append(item)
                item = None
            J.queue.pop(0)
            ind += 1

        while q_items:#re-populate original queue
            J.add(q_items[0])
            q_items.pop(0)
    else:
        raise ValueError("No item to swap with")

def lifo_fifo_queue_print(inp_queue):#used for testing and printing out results from FIFO and LIFO queues' methods 
    print("Queue:",inp_queue.queue)
    swap_with_front(inp_queue, 2)
    print(f"State of queue post swap: {inp_queue.queue}")
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
    fifo_queue.add((1,3.53,"4"))
    fifo_queue.add("lol")

    print("FIFO queue:")
    lifo_fifo_queue_print(fifo_queue)
    print("\n")

    #LIFO queue
    lifo_queue = LifoQueueObj()

    lifo_queue.add({})
    lifo_queue.add([{}])
    lifo_queue.add((6,[],"4", {}))
    lifo_queue.add("wau")

    print("LIFO queue:")
    lifo_fifo_queue_print(lifo_queue)
    print("\n")

    #priority queue
    priority_queue = PriorityQueueObj(maxsize=7)

    priority_queue.add(3)
    priority_queue.add([[1,2]], priority_num=7)
    priority_queue.add({}, priority_num=3)
    priority_queue.add(4.124)
    priority_queue.add("wello", priority_num=12)
    priority_queue.add(219, priority_num=10)
    #priority_queue.add(219, priority_num=10)
    priority_queue.add(21, priority_num=2)
    print(f"Full check: {priority_queue.is_full()}")

    print("Priority Queue:",priority_queue.queue)
    print(f"Priority Queue get: Highest Priority Object: {priority_queue.get()}, Specific Priority (7): {priority_queue.get(7)}")
    print(f"Final priority queue: {priority_queue.queue}, Full check: {priority_queue.is_full()}, Empty check: {priority_queue.is_empty()}")
    
    while not priority_queue.is_empty():
        priority_queue.get()
    print(f"Empty priority queue: {priority_queue.queue}, Full check: {priority_queue.is_full()}, Empty check: {priority_queue.is_empty()}\n")
    

