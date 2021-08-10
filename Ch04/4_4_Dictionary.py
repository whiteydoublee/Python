"""
날짜 : 2021/08/10
이름 : 김예은
내용 : 파이썬 자료구조 Dictionary 실습하기 textbook p98
"""

#Dictionary (Key,Value)
dic1 = {
    'A':'Apple',
    'B':'Banana',
    'C':'Cherry'
} #JSON 구조 (JSON 객체, but dictionary는 자료구조

print('dic1 type: ',type(dic1))
print('dic1:',dic1)
print("dic1['A']:",dic1['A'])
print("dic1['B']:",dic1['B'])
print("dic1['C']:",dic1['C'])

dic2 = {
    1:'서울',
    2:'대구',
    3:'대전',
    4:'광주',
    5:'부산'
}

print('dic2[1]:', dic2[1])
print('dic2[4]:', dic2[4])

dic3={
    101:[1, 2, 3, 4, 5],
    102:(6,7,8,9,10),
    103:{'한국','미국','브라질','세르비아'},
    104:{'p1':'Jennie', 'p2':'Jose', 'p3':'Gordon'}
}

print('dic3 type:', type(dic3))
print('dic3[101][2]: ',dic3[101][2])
print('dic3[102][1]: ',dic3[102][1])
print('list(dic3[103])[0]: ',list(dic3[103])[0])
print("dic3[104]['p2']: ",dic3[104]['p2'])

#응용
dics=[dic1, dic2, dic3]

print('dics',dics)