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
            operator.add, map(lambda m: self.__convert(m, currency), self.moneys), 0
        )
        return Money(total, currency)
    def __convert(self, money, currency):
        eurToUsd = 1.2
        if money.currency == currency:
            return money.amount
        else: return money.amount*eurToUsd
