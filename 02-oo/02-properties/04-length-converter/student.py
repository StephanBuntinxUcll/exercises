
class LengthConverter:

    def __init__(self):
        self.distance_in_meters = 0

    @property
    def meter(self):
        return self.distance_in_meters
    
    @property 
    def feet(self):
        self.distance = self.distance_in_meters * 3.28084
        return self.distance
    
    @property
    def inch(self):
        self.distance = self.distance_in_meters * 39.3701
        return self.distance
    

    @meter.setter
    def meter(self, distanceM):
        self.distance_in_meters = distanceM
        return self.distance_in_meters
    
    @feet.setter
    def feet(self,distanceF):
        self.distance = distanceF
        self.distance_in_meters = distanceF / 3.28084
        return self.distance
    
    @inch.setter
    def inch(self, distanceI):
        self.distance = distanceI
        self.distance_in_meters = distanceI / 39.3701
        return self.distance
    


# length = LengthConverter()


# length.meters = 10

converter = LengthConverter()
converter.meters = 10
print(converter.inch) 

# print(length.meters)
# print(length.feet)
# print(length.inch)
# print(length.distance_in_meters)

# print("//")

# length.meters = 5

# print(length.meters)
# print(length.feet)
# print(length.inch)


