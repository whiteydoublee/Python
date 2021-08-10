"""
날짜 : 2021/08/10
이름 : 김예은
내용 : 파이썬 자료구조 Tuple 실습하기 textbook p84
"""

#Tuple (고정리스트)
tuple1 = (1,2,3,4,5)
print('tuple1 type:', type(tuple1))
print('tuple1[0]: ', tuple1[0])
print('tuple1[2]: ', tuple1[2])
print('tuple1[3]: ', tuple1[3])

tuple2 = ('서울','대전','대구','광주','부산')
print('tuple2 type:', type(tuple2))
print('tuple2[0]: ', tuple2[0])
print('tuple2[2]: ', tuple2[2])
print('tuple2[3]: ', tuple2[3])

#Tuple 수정, 삭제
tuple3 = 1,2,3,4,5 #() 생략 가능

tuple3[0]=7
print('tuple3:',tuple3) #고정리스트이므로 수정 불가

