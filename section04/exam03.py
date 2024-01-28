id = int(input('4자리 사원번호를 입력하세요 >>> '))
num = id%10

print('오전' if num >= 5 else '오후')