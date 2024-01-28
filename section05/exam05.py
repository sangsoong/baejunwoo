car = input('차량번호를 입력하세요 >>> ')
num = int(car[-4:])

if num%2 == 0:
    print(f'차량번호 \'{car}\'는 오늘 운행가능입니다.')
else:
    print(f'차량번호 \'{car}\'는 오늘 운행불가능입니다')