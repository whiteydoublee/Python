"""
날짜: 2021/08/27
이름: 김예은
내용: 코딩테스트-왕실의 나이트
"""

#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
#ord()함수: 특정한 한 문자를 아스키 코드 값으로 변환시켜주는 함수
column = int(ord(input_data[0])) - int(ord('a'))+1

#경우의 수를 모두 생각해보기
result = 0

movements = [(-1,2),(1,2),(-1,-2),(1,-2),(-2,1),(-1,-2),(2,1),(2,-1)]

for movement in movements:
    next_row = row + movement[0]
    next_column = column + movement[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
"""
#오2 위 1
next_row = row - 1
next_column = column + 2

if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
    result+=1



#오2 아 1
next_row = row + 1
next_column = column +2

if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
    result+=1

#왼2 위 1
next_row = row -1
next_column = column -2

if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
    result+=1

#왼2 하 1
next_row = row +1
next_column = column -2

if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
    result+=1

#위2 오1
next_row = row -2
next_column = column +1

if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
    result+=1

#위2 왼1
next_row = row -2
next_column = column - 1

if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
    result+=1

#하2 오1
next_row = row +2
next_column = column +1

if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
    result+=1

#하2 왼1
next_row = row +2
next_column = column -1

if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
    result+=1
"""



print(result)

"""
steps = [(-2,-1),(-1,-2),(1,-2),(1,2),(2,-1),(-2,1),(-1,2),(2,1)]

result =0
for step in steps:
        #이동하고자 하는 위치 확인
    next_row = row +step[0]
    next_column = column + step[1]
    #해당위치로 이동이 가능하다면 카운트 증가
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result+=1
"""