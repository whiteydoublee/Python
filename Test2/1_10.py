"""
날짜: 2021/08/13
이름: 김예은
내용: 파이썬 가위,바위,보 게임
"""
dataset = [5,10,18,22,35,55,75,103,152]
value = int(input('검색할 숫자 입력 :'))

start=0
end = len(dataset)-1
loc = 0
state = False

import random

def game():
    words=['가위','바위','보']
    while True:
        you_word = input('가위, 바위, 보 입력:')
        try:
            if you_word not in words:
                raise ValueError
        except ValueError:
            print('잘못 입력 하셨습니다.')
            continue
        else:
            break


    com_word= random.choice(words)
    print('컴퓨터 결과: ',com_word)

    if com_word == '가위' and you_word =='가위':
        print('무승부')
    elif com_word =='가위' and you_word=='바위':
        print('당신의 승리!')
    elif com_word =='가위' and you_word=='보':
        print('컴퓨터의 승리!')
    elif com_word =='바위' and you_word=='가위':
        print('컴퓨터의 승리!')
    elif com_word =='바위' and you_word=='바위':
        print('무승부')
    elif com_word =='바위' and you_word=='보':
        print('당신의 승리!')
    elif com_word =='보' and you_word=='바위':
        print('당신의 승리!')
    elif com_word =='보' and you_word=='가위':
        print('컴퓨터의 승리!')
    elif com_word =='보' and you_word=='보':
        print('무승부')

while True:
    game()
    print('0: 종료, 1: 한 번 더하기')
    again = int(input('입력:'))

    if again == 0:
        break

print('게임 종료 ...')