class RingBuffer:
    #Constuctor initilize and define buffer
    def __init__(self, capacity):
        #create empty array to hold list
        self.buffer = []
        #set capacity
        self.capacity = capacity
        #define id and set as 0 
        self.id = 0

    #Helper function to iterate id values
    def iterate_id(self):
        #using id values 0 to capacity minus 1
        #resest id to 0 if capacity is reached
        if self.id >= self.capacity - 1:
            self.id = 0
        #or add one to id
        else:
            self.id += 1

    #function to append items
    def append(self, item):
        #check length of array to capacity if 
        #array is full over write the item with 
        #the current id
        if len(self.buffer) == self.capacity:
            #replace item with current id
            self.buffer[self.id] = item
            #jump to next id
            self.iterate_id()
            #if array is not full add to buffer
        else:
            self.buffer.append(item)
            #iterate to next id
            self.iterate_id()


    def get(self):
        return self.buffer
            
