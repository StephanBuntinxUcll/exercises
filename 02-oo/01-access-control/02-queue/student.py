class Queue:

    def __init__(self):
        self.__items = []
    
    def add(self,item):
        return self.__items.append(item)
    
    def next(self):
        return self.__items.pop(0)
    
    def is_empty(self):
        return len(self.__items) == 0
    

rij = Queue()

rij.add("ab")
rij.add("cd")
rij.add("marie")
rij.add("Karel")
rij.add("buntinx")
print(rij.__items)
rij.next()
rij.next()
rij.next()
print(rij.is_empty())


print(rij.__items)