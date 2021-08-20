"""
날짜: 2021/08/20
이름: 김예은
내용: 코딩테스트 - 시각
"""

#h(시) 값 입력받기
h=int(input())
count=0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            #매 시각안에 3이 포함되어 있다면, 카운트 ++
            if '3'in str(i)+str(j)+str(k):
                count+=1

print(count)
