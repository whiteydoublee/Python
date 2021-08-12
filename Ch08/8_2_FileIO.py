"""
날짜: 2021/08/12
이름: 김예은
내용: 파이썬 파일 입출력 실습하기 교재 p217
"""

#파일 읽기
file1=open('./Test1.txt','r')
line = file1.readline()

print(line)
file1.close()

file2 = open('./Test1.txt','r')

while True:
    line = file2.readline()
    if not line: #파일 내용이 없으면,
        break

    print('file2:',line)

file2.close()

#파일 쓰기
file3 = open('./Test2.txt','w',encoding='utf8')
file3.write('안녕하세요\n')
file3.write('감사합니다.\n')
file3.write('안녕히가세요\n')

file3.close()