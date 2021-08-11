#자동차 클래스 정의 Car : module, sub1 : package
class Car:
    # init: 생성자/ 속성을 정의
    def __init__(self,model,color,price):
        # 속성 #self.변수이름
        self.model = model
        self.color = color
        self.price = price

    #기능
    def speedUp(self):
        print('%s speed Up...'%self.model)

    def speedDown(self):
        print('%s speed Down...'%self.model)

    def show(self):
        print('차량명:', self.model)
        print('차량색:', self.color)
        print('차량가격:', self.price)
