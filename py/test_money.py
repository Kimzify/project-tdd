import unittest
from money import Money
from portfolio import Portfolio

class TestMoney(unittest.TestCase):

    def testMultiplication(self):
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
    def testAdditionDollarAndEuros(self):
        fiveDollars = Money(5, 'USD')
        tenEuros = Money(10, 'EUR')
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedResult = Money(17, 'USD')
        actualResult = portfolio.evaluate('USD')
        self.assertEqual(expectedResult, actualResult)



if __name__ == '__main__':
    unittest.main()
