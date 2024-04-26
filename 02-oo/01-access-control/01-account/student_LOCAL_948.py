class Account:

    def __init__(self, login, password):
        self.login = login
        self.password = password


    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self):
        return self.password

    def is_correct_password(self, pw):
        return pw == self.password
    


Jeff = Account("jeff1", "hello")


print(Jeff.is_correct_password("hello"))


