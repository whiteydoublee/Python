from Ch06.sub1.Account import Account

#Inheritance : class 이름(상속할 부모 클래스이름)
class StockAccount(Account):

    def __init__(self,bank,id,name,balance,stock,amount,price):
        super().__init__(bank,id,name,balance)

        self.stock = stock
        self.amount = amount
        self.price = price

    def sell(self,amount, price):
        self._balance+=amount*price
    def buy(self,amount,price):
        self._balance -=amount*price

    def show(self):
        print('-------------------------------------')
        print('은행명: ', self._bank)
        print('계좌번호: ', self._id)
        print('입금주: ', self._name)
        print('현재잔액: ', self._balance)
        print('주식종목:',self.amount)
        print('주식가격:',self.price)
        print('-------------------------------------')