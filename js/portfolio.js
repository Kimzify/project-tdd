const Money = require('./money')
class Portfolio{
    constructor() {
        this.moneys = []
    }
    add(...moneys){
        this.moneys = moneys // in book: this.money.concat(moneys)

    }
    evaluate(currency){
        let total = this.moneys.reduce((sum, money)=>{
            return sum + this.convert(money, currency)
        }, 0)
        return new Money(total, currency)
    }
    convert(money, currency){
        let exchangeRate = new Map()
        exchangeRate.set('EUR->USD', 1.2)
        exchangeRate.set('USD->KRW', 1100)
        let key = money.currency + '->' + currency
        if(money.currency === currency){
            return money.amount
        }
        return money.amount * exchangeRate.get(key)
    }
}
module.exports = Portfolio