"""
날짜: 2021/08/12
이름: 김예은
내용: 파이썬 캡슐화 실습하기 교재 p161
"""

from Ch06.sub1.Account import Account
# private : __(2), protected :_(1)
kb = Account('국민은행','102-111-5555','김유신',100000)

kb.deposit(41000)
kb.withdraw(50000)

#kb.__balance-=1 #취약코드 (캡슐화: 취약코드를 예방하기 위함)
kb.show()

#객체 = 참조변수