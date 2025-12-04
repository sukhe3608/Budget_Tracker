from datetime import datetime

class Transaction:
    def __init__(self, amount: float, category: str, t_type: str, date: str = None):
        self.amount = amount
        self.category = category
        self.type = t_type  # income or expense
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "type": self.type,
            "date": self.date
        }
