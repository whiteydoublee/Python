"""
날짜: 2021/08/12
이름: 김예은
내용: 파이썬 이진검색 연습문제
"""

dataset = [5,10,18,22,35,55,75,103,152]
value = int(input('검색할 숫자 입력 :'))

start=0
end = len(dataset)-1
loc = 0
state = False

while start <=end:
    mid = (start+end)//2

    if dataset[mid] > value:
        end = mid-1
    elif dataset[mid]<value:
        start = mid+1
    else:
        loc = mid
        state = True
        break

if state:
    print('찾은 위치: %d 번째'%(loc+1))
else:
    print('찾는 숫자가 없습니다.')