"""
날짜 : 2021/08/11
이름 : 김예은
내용: 파이썬 객체지향 프로그래밍 실습하기 교재 p148
"""

#객체 생성
from Ch06.sub1.Car import Car #from package import module
from Ch06.sub1.Account import Account

bmw = Car('520d','흰색',5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

benz = Car('벤츠','검정색',7000)
benz.speedUp()
benz.speedDown()
benz.show()

kb = Account('국민은행','101-12-1111','김유신',100000)
kb.deposit(40000)
kb.withdraw(5000)
kb.show()

wr = Account('우리은행','101-12-2222','김춘추',500000)
wr.deposit(50000)
wr.withdraw(100000)
wr.show()

