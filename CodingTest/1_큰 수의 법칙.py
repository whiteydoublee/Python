"""
날짜 : 2021/08/13
이름 : 김예은
내용: 코딩테스트 - 큰 수의 법칙
"""

#n,m,k를 공백으로 구분하여 입력받기
n,m,k=map(int,input().split())

#n개의 숫자를 공백으로 구분하여 입력받기 ( list로 입력받음)
data = list(map(int,input().split()))
#내림차순으로 정렬해야함(큰 수를 구해야하기때문에 큰 수가 앞에와야하므로)
data.sort(reverse=True)

result = 0

repeat=k

#가장 큰 수, 두 번째로 큰 수
first = data[0]
second = data[1]

for i in range(m):

    if repeat >0:
        result += first
        repeat-=1
    else:
        result+=second
        #다시 k의 원래값으로 돌아감.
        repeat=k

"""
i= m//(k+1)
mod = m%(k+1)
result = first*i*k+second*i

if mod !=0:
    result+=mod*first
"""
#최종답안 출력
print(result)

