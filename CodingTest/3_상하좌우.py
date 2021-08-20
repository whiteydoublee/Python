"""
날짜: 2021/08/20
이름: 김예은
내용: 코딩테스트 - 상하좌우
"""

#n값 입력받기
n = int(input())
x,y = 1,1
plans = input().split() #split 분리해서 list로 변환


for plan in plans:
    if plan == 'L':
        if y==1:
            continue
        else:
            y-=1

    elif plan == 'R':
        if y== n:
            continue
        else:
            y += 1

    elif plan == 'U':
        if x == 1:
            continue
        else:
            x -= 1
    elif plan == 'D':
        if x == n:
            continue
        else:
            x += 1

print(x,y)