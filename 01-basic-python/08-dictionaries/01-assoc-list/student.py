

class AssocList:

    def __init__(self):
        self.__item = []



    def __setitem__(self, key, value):
        for pair in self.__item:
            if pair[0] == key:
                pair[1] = value
                break
        else:      
            return self.__item.append(list((key,value)))
    
    def printitem(self):
        for key, value in self.__item:
            print(f"key: {key} value: {value}")

    def __getitem__(self,key):
        for k,v in self.__item:
            if k == key:
                return print( f"{v}")
        else:
            raise KeyError("Does not exist")
        
    def getlenght(self):
        return print(len(self.__item))
    
    
test = AssocList()

result = test.__setitem__("hond","dog")
result = test.__setitem__("kat","cat")
result = test.__setitem__("draak", "draon")
result = test.__setitem__("kat", "cot")
result = test.__setitem__("vis", "fish")
result = test.__setitem__("draak", "dragon")
# test.__getitem__("draak")

test.getlenght()

test.printitem()
            
