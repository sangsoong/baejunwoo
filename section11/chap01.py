'''
사용자 정의 함수
'''

def greet(message, count):
    for i in range(count):
        print(message)
        
greet('asd', 3)

def add(num1:int, num2:int)->int:
    return num1 + num2

print(add(1, 2))

def say_hello():
    print('안녕하세요, 반갑습니다')

def pi():
    return 3.14

num3 = add(1.1, 3.5)
print(num3)
num3 = add(1.1, 3)
print(num3)
num3 = add('안녕하세요', '반갑습니다')
print(num3)
num3 = add(num3, '!')
print(num3)

def upper_case(message:str)->str:
    return message.upper()