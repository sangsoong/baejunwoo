'''
파일 입출력

파일 종류 : 텍스트 파일, 바이너리 파일

파일 입력 : 읽기
파일 출력 : 저장

file mode
r : 읽기
w : 쓰기
a : 추가

t : 텍스트
b : 바이너리
'''

path = 'C:\\Users\\User\\Documents\\baejunwoo\\section13\\test.txt'

#
file = open(path, 'r')

str = file.read()
lines = str.split('\n')
print(str)
print(lines)

file.close()

print('파일 닫힘')

#
with open(path, 'r') as file:
    print(file.read())

print('파일 닫힘')