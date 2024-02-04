'''
메소드: 어떤 객체가 가지고있는 함수
'''

# 문자열의 메소드
val = 123
print(f'10자리 폭 왼쪽정렬 "{val:<10}"')

val = 42.195
print(f'10자리 폭 왼쪽정렬 "{val:<10.1f}"')

# count
s = 'Hello Python!'
print(s.count('o', 6)) # 6번째 인덱스에서부터 찾기

s = 'Hello Python Python Python Python'
print(f'문자열 {s}에서 Python은 {s.count('Python')}개 있습니다.')

# find : 실패시 -1반환
print(f'{s}에서 첫번째 "o"는 인덱스 {s.find('o')}에 있습니다')
print(f'{s}에서 첫번째 "z"는 인덱스 {s.find('z')}에 있습니다')
print(f'{s}에서 첫번째 "Python"는 인덱스 {s.find('Python')}에서 시작합니다')

# index : 실패시 에러
print(f'{s}에서 첫번째 "o"는 인덱스 {s.index('o')}에 있습니다.')
#print(f'{s}에서 첫번째 "z"는 인덱스 {s.index('z')}에 있습니다.')

# upper, lower
print(s.upper())
print(s.lower())

# join
print('-'.join(['010','1234','5678']))
print(' '.join('Python'))
print(''.join(['1','2','3','4','5']))

# split
print(s.split())
print('010-1234-5678'.split('-'))

# replace
print(s.replace('P', 'p'))
print(s.replace('Python', 'py'))

# lstrip, rstrip, strip
s = '     Python     '
print('left' + s.lstrip() + 'right')
print('left' + s.rstrip() + 'right')
print('left' + s.strip() + 'right')