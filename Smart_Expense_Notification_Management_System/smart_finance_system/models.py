from datetime import datetime
class Expense:
    def __init__(self, amount, category, date = None):
        self.amount = amount
        self.category = category
        if date: 
            self.date = date
        else: 
            self.date = datetime.now().strftime("%d%m%Y %H:%M")
            
    def __str__(self):
        return f"{self.amount} TL - {self.category} "

class Budget:
    def __init__(self, limit):
        self.limit = limit
        self.expenses = []
        
    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total 
        
    def average_expense(self):
        if len(self.expenses) == 0:
            avg = 0
        else:
            avg = self.total_expense() / len(self.expenses)
        return avg
        
    def is_limit_exceeded(self):
        if self.total_expense() > self.limit:
            return True
        else:
            return False
            