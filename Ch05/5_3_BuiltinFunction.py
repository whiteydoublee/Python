"""
날짜 : 2021/08/11
이름 : 김예은
내용: 파이썬 내장함수 실습하기 교재 p118
"""
#내장함수: 파이썬은 내장함수 사용전, 수동으로 선언해주어야함.
#시간,수학 함수

import time
import math
import random

#time #######################################

t1 = time.time()
print('t1: ',t1) #Unix TimeStamp(기준:01.01.1970 from 00:00~present)

t2= time.ctime() #변환된 Unix Time
print('t2: ',t2)

now = time.localtime(time.time()) #날짜의 개별
year= time.strftime('%Y',now) # 소문자 y : 연도 두 자리
month= time.strftime('%m',now)
date= time.strftime('%d',now)
hour= time.strftime('%H',now)
min= time.strftime('%M',now)
second= time.strftime('%S',now)

print('%s년 %s월 %s일'%(year,month,date))
print('{}시 {}분 {}초'.format(hour,min,second))

#math #######################################
#abs : 절대값
r1=abs(-5)
print('r1:',r1)

#ceil : 올림(다음 정수로 무조건 올림)
r2=math.ceil(1.2)
r3=math.ceil(1.8)
print('r2:',r2)
print('r3:',r3)

#floor: 내림
r4=math.floor(1.2)
r5=math.floor(1.9)
print('r4:',r4)
print('r5:',r5)

#round: 반올림 (math를 쓰지 않음)
r6 = round(1.2)
r7 = round(1.8)
print('r6:',r6)
print('r7:',r7)

#random (임의의 수:0~1사이의 임의의 실수)
num1 = random.random()
print('num1:',num1)

num2 = num1 *10
print('num2:',num2) #0~10사이의 임의의 실수

num3 = math.ceil(num2) #1~10사이의 정수
print('num3:',num3)

result = math.ceil(random.random()*10)
print('result:',result)

