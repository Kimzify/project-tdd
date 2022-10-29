const assert = require('assert')
const Money = require('./money')
const Portfolio = require('./portfolio')

class MoneyTest{
    testMultiplication(){
        let tenEuros = new Money(10, 'EUR')
        let twentyEuros = new Money(20, 'EUR')
        assert.deepStrictEqual(twentyEuros, tenEuros.times(2))
    }
    testDivision(){
        let originalMoney = new Money(4002, 'KRW')
        let expectedMoneyAfterDivision = new Money(1000.5, 'KRW')
        assert.deepStrictEqual(originalMoney.divide(4), expectedMoneyAfterDivision )
    }
    testAddition(){
        let fiveDollars = new Money(5, 'USD')
        let tenDollars = new Money(10, 'USD')
        let fifteenDollar = new Money(15, 'USD')
        let portfolio = new Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        assert.deepStrictEqual(portfolio.evaluate("USD"), fifteenDollar)
    }
    runAllTests(){
        let testMethods = this.getAllTestMethods()
        testMethods.forEach(m=>{
            console.log("Running: %s()", m)
            let method = Reflect.get(this,m);
            try{
                Reflect.apply(method, this, [])
            }catch (e){
            if (e instanceof assert.AssertionError) {
                    console.log(e);
                } else {
                    throw e;
                }
            }
        })
    }
    getAllTestMethods() {
        let moneyPrototype = MoneyTest.prototype
        let allProps = Object.getOwnPropertyNames(moneyPrototype)
        let testMethods = allProps.filter(p=> typeof moneyPrototype[p] === "function" && p.startsWith('test'))
        return testMethods
    }
    testAdditionOfDollarsAndEuros(){
        let fiveDollars = new Money(5, 'USD')
        let tenEuros = new Money(10, 'EUR')
        let portfolio = new Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        let expectedValue = new Money(17, 'USD')
        assert.deepStrictEqual(expectedValue, portfolio.evaluate('USD'))
    }
    testAdditionOfDollarsAndWons(){
        let oneDollar = new Money(1, 'USD')
        let elevenHundredWon = new Money(1100, 'KRW')
        let portfolio = new Portfolio()
        portfolio.add(elevenHundredWon, oneDollar)
        let expectedValue = new Money(2200, 'KRW')
        assert.deepStrictEqual(expectedValue, portfolio.evaluate('KRW'))
    }
}


new MoneyTest().runAllTests()