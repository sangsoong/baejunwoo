'''
조건문
'''

# 들여쓰기 : 분기점
num1 = 10
num2 = 5
if num1 == 10 and num2 == 5:
    print(num1)
    print(num2)

print('조건문 처리가 끝났습니다.')

# else
if num1 == 10:
    print(f'{num1}은 10입니다')
else:
    print(f'{num1}은 10이 아닙니다.')
    
# 참거짓
isOk = True
li = []
nothing = ""
num1 = 0

if isOk:
    print(isOk)

if li:
    print(li)

if nothing:
    print(nothing)
    
if num1:
    print(num1)
    
# 2중
if num1 == 10:
    if num2 == 5:
        print('num1이 10이고 num가  5이다.')
    print('num1이 10이고 num2는 5가 아니다.')
print('num1는 10이아니고 num2는 5가아니다.')