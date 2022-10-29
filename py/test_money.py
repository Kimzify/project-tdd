import unittest
import functools
import operator
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    def times(self, multiplier):
        return Money(multiplier*self.amount, self.currency)
    def divide(self,divisor):
        return Money(self.amount/divisor, self.currency)
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

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

class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self):
        fiver = Money(5, 'USD')
        tenner = fiver.times(2)
        self.assertEqual(tenner, fiver.times(2))

    def testMultiplicationInEuros(self):
        tenEuros = Money(10, 'EUR')
        twentyEuros = tenEuros.times(2)
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivision(self):
        originalMoney = Money(4002, 'KRW')
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, 'KRW')
        self.assertEqual(actualMoneyAfterDivision, expectedMoneyAfterDivision)

    def testAddition(self):
        fiveDollars = Money(5, 'USD')
        tenDollars = Money(10, 'USD')
        fifteenDollars = Money(15, 'USD')
        portfolio = Portfolio()
        portfolio.add(fiveDollars,tenDollars )
        self.assertEqual(fifteenDollars, portfolio.evaluate('USD'))


if __name__ == '__main__':
    unittest.main()
