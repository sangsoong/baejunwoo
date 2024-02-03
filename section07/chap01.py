'''
파이썬에서의 for 반복문 : 일반적으로 시퀀스(순서가 있는 것, 인덱싱이 가능한 것)와 같이 사용된다, 비시퀀스와 사용되는 경우도 있다
'''

li = [10, 20, 30, 50, 80, 100]
for num in li:
    print(num)
    
s = 'Hello Python!'
for ch in s:
    print(ch)
    
tp = tuple(li)
for num in tp:
    print(num)
    
li = ['파이썬', '자바', 'C/C++', '코틀린']
for s in li:
    print(s)
    
# range(n) : 0 ~ n-1 까지의 데이터가 생성된다
li = list(range(5))
print(li)

# range(a, b) : a ~ b-1 까지의 데이터가 생성된다
li = list(range(5, 10))
print(li)

# range(a, b, c) : a ~ b-1 까지의 데이터가 c의 간격으로 생성된다
li = list(range(1, 10, 2))
print(li)

# 1 ~ 5 까지 반복
for num in range(1, 6):
    print(num, end='\t')
    
# 5번 반복
for num in range(5):
    print('Hello Python')
    
dan = int(input('구구단을 출력할 단수를 입력하세요 >>> '))
for gop in range(1, 10):
    print(f'{dan} * {gop} = {dan*gop}')