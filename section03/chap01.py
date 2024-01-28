'''
기본적인 출력문
'''

print('test1', 'test2', 'test3')            # 기본(각 개체를 띄어쓰기로 구분)
print('test1', 'test2', 'test3', sep='')    # 각 객체를 공백으로 구분
print('test1', 'test2', 'test3', sep='-')   # 각 개체를 -로 구분
print('test1', 'test2', 'test3', sep='\t')  # 각 개체를 탭으로 구분
print('test1', 'test2', 'test3', sep='\n')  # 각 개체를 개행으로 구분

print('test1', 'test2', 'test3', sep='\t', end=' :: ')  # 문자열의 끝을 ' :: '으로 지정
print('test1', 'test2', 'test3', sep='\t')              # 기본(문자열의 끝을 개행으로 지정)

'''
형식을 갖는 문자열
'''

# 포맷 연산자 %를 이용
# %d : 정수
# %o : 8진수
# %x : 16진수
# %f : 실수
# %s : 문자열
print('%d'%10)
age = 19
height = 165.5
name = '배준우'
print('제 나이는 %d살, 키는 %fcm이고, '%(age, height), '이름은 %s 입니다.'%name)
print('%d, %o, %x'%(10, 10, 10))

print('%5d'%0, '|')     # '    1' 다섯칸 확보 후 오른쪽정렬
print('%-5d'%0, '|')    # '1    ' 다섯칸 확보 후 왼쪽정렬
print('%.3f'%3.14)      # '3.140' 소수점 아래 3자리까지 표시
print('%6.3f'%3.14)     # ' 3.140' 여섯칸 확보 후(소수점 포함) 오른쪽정렬로 소수점 아래 3자리까지 표시

# format() 메소드를 이용
print('{} {}'.format(1, 2))
print('{3} {0} {2} {1}'.format(1, 2, 3, 4))

# f-string 객체를 이용
print(f'제 나이는 {age}살, 키는 {height}cm이고, 이름은 {name}입니다.')
num1 = int(input('첫번째 수 입력 >>> '))
num2 = int(input('두번째 수 입력 >>> '))
print(f'{num1} + {num2} = {num1 + num2}')