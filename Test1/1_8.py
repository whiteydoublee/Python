"""
날짜: 2021/08/12
이름: 김예은
내용: 파이썬 최대값 최소값 연습문제
"""

scores=[62,82,76,88,54,92]

max = scores[0]
min = scores[0]

for score in scores:

    if max< score:
        max = score
    if min > score:
        min = score

print('최대값: ',max)
print('최소값: ',min)