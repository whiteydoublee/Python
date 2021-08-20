"""
날짜: 2021/08/20
이름: 김예은
내용: 코딩테스트 - 상하좌우
"""

#n값 입력받기
n = int(input())
x,y = 1,1
plans = input().split()

moving_step = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for plan in plans:
    for i in range(len(moving_step)):
        if plan == moving_step[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    if nx < 1 or ny <1 or nx > n or ny>n:
        continue
    x,y = nx, ny

print(x,y)