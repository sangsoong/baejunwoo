count = 5
password = 'qwerty'

while count > 0:
    get = input(f'비밀번호를 입력해주세요(남은횟수:{count}) >>> ')
    
    if get == password:
        print('비밀번호를 맞췄습니다.')
        break
    else:
        print('비밀번호를 틀렸습니다.')
        count -= 1
    
    print('==============================')

if count == 0:
    print('비밀번호 입력 횟수를 초과했습니다.')