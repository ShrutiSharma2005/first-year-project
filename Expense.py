# define a class called expense
class Expense:
    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

    #define a class called _repr_
    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"


