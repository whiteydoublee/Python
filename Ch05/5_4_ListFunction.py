"""
날짜 : 2021/08/11
이름 : 김예은
내용: 파이썬 리스트함수 실습하기 교재 p98
"""

import math

dataset=[1,4,3]
print('1-dataset:',dataset)

#데이터 추가: .append()
dataset.append(2)
dataset.append(5)
print('2-dataset:',dataset)

#데이터 정렬 : sort() - ASC
dataset.sort()
print('3-dataset:',dataset)

# sort(revers=True): DESC
dataset.sort(reverse=True)
print('4-dataset:',dataset)

#데이터 뒤집기
dataset.reverse()
print('5-dataset:',dataset)

#데이터 삽입
dataset.insert(2,6) #insert(index num, 입력할 값)
print('6-dataset:',dataset)

#데이터 삭제 : remover(삭제할 값 입력)
dataset.remove(6)
print('7-dataset:',dataset)

#map함수 : 리스트의 데이터를 지정된 함수에 일괄처리해주는 함수
def plus10(n):
    return n+10

list1=[1,2,3,4,5]
r1= map(plus10, list1)
print('r1:',list(r1)) #map 객체 -> list로 변환

list2=[0.1,1.2,2.6,3.4,4.9]
r2= map(math.ceil,list2) #Java Stream과 비슷
print('r2:',list(r2))

list3 =['1','2','3','4','5']
r3 = map(int, list3) #String -> int 형태로 일괄 변환
print('r3: ',list(r3))