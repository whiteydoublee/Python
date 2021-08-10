"""
날짜 : 2021/08/10
이름 : 김예은
내용 : 파이썬 자료구조 Set 실습하기 textbook p96
"""

#Set : 인덱스 번호가 없음, 순서가 없어서 -> 개별로 출력 원하는 경우, List로 타입을 변환하여 출력
set1 = {1, 2, 3, 4, 5, 3, 2}
print('set1 type:', type(set1))
print('set1:',set1)

set2 = set('Hello World')
print('set2 type:', type(set2))
print('set2:',set2)

#리스트 벼환 후 출력
list1 = list(set1)
print('list1 : ',list1)
print('list1[0]:', list1[0])
print('list1[2]:', list1[2])
print('list1[3]:', list1[3])

list2 = list(set2)
print('list2 : ',list2)
print('list2[0]:', list2[0])
print('list2[2]:', list2[2])
print('list2[3]:', list2[3])