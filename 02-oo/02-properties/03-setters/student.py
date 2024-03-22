# Write your code here

class Time:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, value):
        if value < 0 or value > 23:
            raise ValueError("must be a hour between 0 and 23 ")
        self.__hours = value


    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def seconds(self):
        return self.__seconds
    
    @minutes.setter
    def minutes(self, value):
        self.__checktime(value)
        self.__minutes = value

    @seconds.setter
    def seconds(self, value):
        self.__checktime(value)
        self.__seconds = value
        
    def __str__(self):
        return f"{self.hours} : {self.minutes} : {self.seconds}"
    
    def __checktime(self, value):
        if value <0 or value > 59:
            raise ValueError("must be between 0 an 59")
        

        


time = Time(12,2,6)

time.hours = 8
time.minutes = 32
time.seconds = 40

print(time)