class queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def hot_potato(name_list,num):
    sim_queue=queue()
    for i in name_list:
        sim_queue.enqueue(i)
    while sim_queue.size()>1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()
l=["arjun","prasad","sravan","bokka","vineeth","varma"]
print(hot_potato(l,8))

        