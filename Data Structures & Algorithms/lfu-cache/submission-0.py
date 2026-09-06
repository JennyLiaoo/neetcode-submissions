class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.values = dict()    #key->val,freq,time
        self.time = 0
        self.lfu = []   #(freq, time, key)  # laxzy deletion


    
    def get(self, key: int) -> int:
        # get val if exists (inc freq),time freq
        self.time+=1
        if key in self.values:
            val,freq,time = self.values[key]
            self.values[key] = (val,freq+1,self.time)
            heapq.heappush(self.lfu, (freq+1,self.time,key))
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return
        # update/insert key,val
        #time, freq
        self.time+=1
        if key in self.values:
            val, freq, time = self.values[key]
            self.values[key] = (value, freq+1,self.time)
            heapq.heappush(self.lfu, (freq+1,self.time,key))

        else:
            while len(self.values) + 1 > self.cap:
                freq,time,oldkey = heapq.heappop(self.lfu)
                if oldkey in self.values and self.values[oldkey][1] == freq and self.values[oldkey][2] == time:
                    self.values.pop(oldkey)
            self.values[key] = (value, 1, self.time)
            heapq.heappush(self.lfu, (1, self.time, key))
            

            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)