"""
날짜: 2021/08/27
이름: 김예은
내용: 코딩테스트-1이 될때까지
"""

#n,k 를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    if n==1:
        break

    if n%k==0:
        n/=k

    else:
        n-=1

    result += 1

print(result)


"""
while n!=1:

    if n%k==0:
        n = n/k
        result +=1
    else:
        n -= 1
        result += 1
"""