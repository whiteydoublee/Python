"""
날짜: 2021/08/09
이름 : 김예은
내용 : 파이썬 문자열 실습하기 교재 p48
"""

#문자열 더하기
str1 = 'Hello, '
str2 = 'Korea'
str3 = str1+str2

print('str3: ',str3)

#문자열 곱하기 (* Number = Number 만큼 반복)
message = 'Hello!'
result = message*3
print('result: ',result)

#문자열 길이
sample ='Hello World'
print('sample 길이: ', len(sample)) #len()은 띄어쓰기 까지 길이 포함

#문자열 인덱스
print('sample 1번째 문자: ',sample[0])
print('sample 7번째 문자: ',sample[6])
print('sample -1번째 문자: ',sample[-1])

#문자열 자르기
print('sample 0~5까지의 문자열 :', sample[0:5])
print('sample 처음~5까지의 문자열 :', sample[:5])
print('sample 6~11까지의 문자열 :', sample[6:11])
print('sample 6~마지막까지의 문자열 :', sample[6:])

#문자열 분리
people = '김유신^김춘추^장보고^강감찬^이순신'
p1,p2,p3, p4, p5=people.split('^')

print('p1:',p1)
print('p2:',p2)
print('p3:',p3)
print('p4:',p4)
print('p5:',p5)

#문자열 이스케이프
print('안녕!\n 파이썬!') #*\n: 이스케이프(개행: 줄바꿈)
print('안녕!\t 파이썬!') #*\t: 이스케이프(tab)
print('안녕!\b 파이썬!') #*\b: 이스케이프(backspace)
print('안녕!\'파이썬!\'') #*\: 이스케이프(문자 ' (따옴표 처리))
print("'안녕!파이썬!'") #*\: 이스케이프(문자 " (따옴표 처리))


