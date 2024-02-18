'''
지역변수와 전역변수
'''

total = 1

def my_func():
    print(total)    # 전역변수 total
    
my_func()
print(total)

def my_func2():
    total = 2
    print(total)    # 지역변수 total
    
my_func2()
print(total)

def my_func3():
    global total    # 전역변수 total
    total = 3
    print(total)
    
my_func3()
print(total)