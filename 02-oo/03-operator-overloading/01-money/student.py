
class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount + other.amount,
                self.currency
            )
        else:
            raise RuntimeError("mismatched currencys")
        
    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount - other.amount,
                self.currency
            )
        else:
            raise RuntimeError("mismatched currencys")
        
    def __mul__(self, multiply):
        return Money(
            self.amount * multiply,
            self.currency
        )

    
        
#     def __str__(self):
#         return f"{self.amount, self.currency}"


# myMoney = Money(50 , "EUR")

# yourMoney = Money(100 , "EUR")

# extraMoney = Money(200, "USD")

# extraMoney2 = Money(75, "USD")

# print(myMoney + yourMoney)
# # print(myMoney + extraMoney)
# print(extraMoney *  5)