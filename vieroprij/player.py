class Player:

    def __init__(self, name, token):
        self.name = name
        self.token = token

        @property
        def name(self):
            return self.__name
        
        @name.setter
        def name(self, value):
            return self.__token