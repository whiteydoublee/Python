"""
날짜 : 2021/08/10
이름 : 김예은
내용 : 파이썬 while문 실습하기
"""

#while
num =1

while num < 5:
   print('%d회 반복'%num)
   num+=1

#1부터 10까지의 합
tot, k=0,1

while k<=10 :

    tot+=k
    k += 1

print('1부터 10까지의 합: ',tot)

#1부터 10까지 짝수합
total , j =0,1

while j<=10:
    if j%2==0:
        total+=j
    j += 1
print('1부터 10까지 짝수합: ',total)

#break : 반복문을 끝낸다. (흐름이 끊김)
i = 1

while True: #무한반복

    if i%5==0 and i%7==0:
        break
    i+=1

print('5와 7의 최소공배수 :',i )

#continue : 반복문의 처음으로 이동 (흐름은 계속된다)
sum, n= 0,1

while n<=10:
    n+=1
    if n%2==1:
        continue #odd number -> 반복문의 처음으로 이동
    sum += n

print('1부터 10까지의 짝수합 :',sum)
