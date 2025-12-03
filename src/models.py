from datetime import datetime

class Transaction:
   def __init__(self, amount:float, date:datetime, t_type:str, category:str):
       self.amount = amount
       self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       self.type = t_type
       self.category = category
       
    def to_dict(self):
        return {
            "amount": self.amount,
            "date": self.date,
            "type": self.type,
            "category": self.category
        }