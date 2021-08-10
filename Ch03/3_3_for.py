"""
날짜 : 2021/08/10
이름 : 김예은
내용 : 파이썬 for 실습하기
"""

#for
for i in range(5):
    print('{}회 반복'.format(i))

for i in range(10,15): #10~15 까지 반복
    print('%d회 반복'%i)

for i in range(5,0,-1): # 5회 반복 (0이 될 때 까지 1씩 빼라)
    print(i,'회 반복')

#1부터 10까지의 합
total = 0

for k in range(11):
    total+=k
print('1~10까지의 합: ', total)

#1부터 10까지의 짝수합
eSum=0

for k in range(11):
    if k%2 ==0:
        eSum += k

print('1부터 10까지의 짝수합:',eSum)

#중첩 for 문
for a in range(3):
    print('a:', a)
    for b in range(5):
        print('b:',b)

#구구단
for x in range(2,10):
    print('%d단'%x)
    for y in range(1,10):
        z=x*y
        print('%d x %d = %d'%(x,y,z))

#별삼각형
for a in range(10):

    for b in range(a):
        print('☆', end='')
    print()

for a in range(11):

    for b in range(10-a):
        print('☆', end='')
    print()

for a in range(10,0,-1):
    for b in range(a):
        print('☆', end='')
    print()

for i in range(11):
    print('★'*i)