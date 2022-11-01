import functools
import operator
from money import Money

class Portfolio:

    def __init__(self):
        self.moneys =[]
    def add(self, *money):
        self.moneys = money
    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, map(lambda m: m.amount, self.moneys), 0
        )
        return Money(total, currency)