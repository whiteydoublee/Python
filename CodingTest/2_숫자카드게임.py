"""
날짜 : 2021/08/13
이름 : 김예은
내용: 코딩테스트 - 숫자카드게임
"""

#n,m을 공백으로 구분하여 입력받기
n,m = map(int, input().split())
#입력된 값 중 적은 값을 저장하기위해 리스트 생성
mins=[]
result =0

for i in range(n):
    #행 데이터 입력하기
    data = list(map(int,input().split()))
    #오름차순 정렬
    data.sort()
    #최소값 구하기
    min =data[0]

    #각 행의 최소값 저장
    mins.append(min)

mins.sort(reverse=True)
result=max(mins)

#최종 답안 출력
print(result)