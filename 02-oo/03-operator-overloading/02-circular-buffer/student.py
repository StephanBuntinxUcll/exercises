
class CircularBuffer:

    def __init__(self, n):
        self.mylist = []
        self.n = n

    def add(self, value):
        self.mylist.append(value)
        if len(self.mylist) > self.n:
            del self.mylist[0]

    
    def __getitem__(self, index):
        return self.mylist[index]
    
    def __len__(self):
        return len(self.mylist)
    
        



# buffer = circularBuffer(3)

# buffer.add(70)
# buffer.add(21)
# print(buffer.mylist)
# buffer.add(123)
# print(buffer.mylist)
# buffer.add(22)
# print(buffer.mylist)
# buffer.add(5)
# print(buffer.mylist)
# print(len(buffer.mylist))