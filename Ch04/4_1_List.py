"""
날짜 : 2021/08/10
이름 : 김예은
내용 : 파이썬 자료구조 실습하기 textbook p84
"""

#list
list1 = [1,2,3,4,5] #Linear 선형 구조
print('list1 type: ', type(list1))
print('list1[0]: ', list1[0])
print('list1[2]: ', list1[2])
print('list1[3]: ', list1[3])

list2 = [ 5, 3.14, True, 'Apple']
print('list2 type: ', type(list2))
print('list2[0]: ', list1[2])
print('list2[3]: ', list1[3])

list3 = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print('list3 Tyep: ',type(list3))
print('list3[0][2]:', list3[0][2])
print('list3[1][2]:', list3[1][2])
print('list3[2][2]:', list3[2][2])


#list 덧셈
ani1 = ['사자','호랑이','곰']
ani2 = ['코끼리','기린']
ani3 = ani1+ani2
print('ani3 : ',ani3)

#list 수정,삭제
#수정
nums=[1,2,3,4,5]

nums[1]= 7
print('nums: ',nums)

nums[2:4]=[8,9,10]
print('nums: ',nums)

#삭제
nums[3:5]=[]
print('nums: ',nums)

#list 반복문
array = [1,2,3,4,5]

for n in array:
    print('n: ',n)

people = ['김유신','김춘추','장보고']
for person in people:
    print(person)

for i, value in enumerate(people): #i : index, value: people 값
    print('people[%d]: %s'%(i,value))

#list Comprehension
numbers = [1, 2, 3, 4, 5]

res1 = [num*3 for num in numbers] # for문의 내용이 앞에 옴. For in List
res2 = [num*3 for num in numbers if num%2==1] #for문의 내용이 앞에 옴. For in List/ 안의 조건문

print('res1: ',res1)
print('res2: ',res2)



