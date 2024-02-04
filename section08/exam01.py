money = 10000

while money > 0:
    print(f'현재 {money}원이 있습니다.')
    use = int(input('사용할 금액을 입력해주세요 >>> '))
    if use > money:
        print(f'잔고가 {use-money}원 부족합니다.')
    elif use <= 0:
        print('0원 이하의 금액을 사용할 수 없습니다.')
    else:
        print(f'{use}원을 사용했습니다.')
        money -= use
    print('-------------------------')

print('잔고가 없습니다.')