'''
파이썬의 특별한 함수 스타일
'''

# 코드의 생략
def pass_func():
    ...

# 가변 매개 변수
def show(*vals:int, horiz:int=0):
    print(vals)
    for n in vals:
        if horiz == 1:
            print(n, end='\t')
        else:
            print(n)
    print()

show(1, 2, 3, 4, 5, horiz=1)
show(1, 2, 3, 4, 5, horiz=0)
show(1, 2, 3, 4, 5)

def greet(message:str, temp:int=2, count:int=1):
    for i in range(count):
        if count == 2:
            return
        print(message)
    print()
        
greet('안녕하세요')
greet('안녕하세요', 2, 2)
greet('안녕하세요', 3, 3)